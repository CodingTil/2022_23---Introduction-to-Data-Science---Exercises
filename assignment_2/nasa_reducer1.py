#!/usr/bin/env python3
import sys

current_execution_id = None
current_activity = None
current_lifecycle_transition = None
current_timestamp = None
total_time = 0

for line in sys.stdin:
    line = line.strip()
    execution_id, activity, lifecycle_transition, timestamp = line.split("\t")
    if current_execution_id is not None:
        if current_execution_id != execution_id:
            print("{}\t{}".format(current_activity, total_time))
            current_execution_id = execution_id
            current_activity = activity
            current_lifecycle_transition = lifecycle_transition
            current_timestamp = float(timestamp)
            total_time = 0
        else:
            if current_lifecycle_transition == "start":
                if lifecycle_transition == "complete":
                    total_time += float(timestamp) - current_timestamp
                else:
                    raise Exception("Unexpected lifecycle transition")
            elif current_lifecycle_transition == "complete":
                if lifecycle_transition == "start":
                    total_time += current_timestamp - float(timestamp)
                else:
                    raise Exception("Unexpected lifecycle transition")
            else:
                raise Exception("Unexpected lifecycle transition")
    else:
        current_execution_id = execution_id
        current_activity = activity
        current_lifecycle_transition = lifecycle_transition
        current_timestamp = float(timestamp)

# Print the last execution_id
print("{}\t{}".format(current_activity, total_time))
