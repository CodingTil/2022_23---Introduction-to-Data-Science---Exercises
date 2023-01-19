#!/usr/bin/env python3
import sys

current_execution_id = None
current_activity = None
current_lifecycle_transition = None
current_timestamp = None
total_time = 0
start_count=0
complete_count=0

for line in sys.stdin:
    line = line.strip()
    execution_id, lifecycle_transition, activity, timestamp = line.split("\t")
    if current_execution_id is not None:
        if current_execution_id != execution_id:
            if start_count > 1 or complete_count > 1:
                raise Exception("Unexpected number of start or complete")
            if start_count == 1 and complete_count == 1:
                print("{}\t{}".format(current_activity, total_time))
            current_execution_id = None
            current_activity = None
            current_lifecycle_transition = None
            current_timestamp = None
            total_time = 0
            start_count=0
            complete_count=0
        else:
            if current_lifecycle_transition == "start":
                if lifecycle_transition == "complete":
                    assert total_time == 0
                    total_time = float(timestamp) - current_timestamp
                    complete_count+=1
                else:
                    raise Exception("Unexpected lifecycle transition")
            elif current_lifecycle_transition == "complete":
                if lifecycle_transition == "start":
                    assert total_time == 0
                    total_time = current_timestamp - float(timestamp)
                    start_count+=1
                else:
                    raise Exception("Unexpected lifecycle transition")
            else:
                raise Exception("Unexpected lifecycle transition")
    else:
        current_execution_id = execution_id
        current_activity = activity
        current_lifecycle_transition = lifecycle_transition
        current_timestamp = float(timestamp)
        if lifecycle_transition == "start":
            start_count+=1
        elif lifecycle_transition == "complete":
            complete_count+=1
        else:
            raise Exception("Unexpected lifecycle transition")

# Print the last execution_id
if start_count > 1 or complete_count > 1:
    raise Exception("Unexpected number of start or complete")
if start_count == 1 and complete_count == 1:
    assert current_activity is not None
    print("{}\t{}".format(current_activity, total_time))
