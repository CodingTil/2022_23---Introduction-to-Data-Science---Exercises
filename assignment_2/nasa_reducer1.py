#!/usr/bin/env python3
import sys

current_execution_id = None
current_activity = None
current_lifecycle_transition = None
current_timestamp = None

for line in sys.stdin:
    line = line.strip()
    execution_id, activity, lifecycle_transition, timestamp = line.split("\t")
    if current_execution_id is not None:
        assert current_execution_id == execution_id
        assert current_activity == activity
        if current_lifecycle_transition == "start":
            if lifecycle_transition == "complete":
                print(f"{activity}\t{float(timestamp) - current_timestamp}")
            else:
                raise Exception("Unexpected lifecycle transition")
        elif current_lifecycle_transition == "complete":
            if lifecycle_transition == "start":
                print(f"{activity}\t{current_timestamp - float(timestamp)}")
            else:
                raise Exception("Unexpected lifecycle transition")
        else:
            raise Exception("Unexpected lifecycle transition")
    else:
        current_execution_id = execution_id
        current_activity = activity
        current_lifecycle_transition = lifecycle_transition
        current_timestamp = float(timestamp)