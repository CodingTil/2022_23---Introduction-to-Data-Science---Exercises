#!/usr/bin/env python3
import sys

current_execution_id = None
current_activity = None
current_lifecycle_transition = None
current_timestamp = None

for line in sys.stdin:
    line = line.strip()
    execution_id, lifecycle_transition, activity, timestamp = line.split("\t")
    if current_execution_id is not None:
        # execution id must match (there are always 2)
        if current_execution_id != execution_id:
            raise Exception("Unexpected execution_id")

        # there must be exactly 1 start and 1 complete
        if not ((current_lifecycle_transition == "start" and lifecycle_transition == "complete")
            or (current_lifecycle_transition == "complete" and lifecycle_transition == "start")):
            raise Exception("Unexpected lifecycle transition")

        if not (current_activity == activity):
            raise Exception("Unexpected activity")

        print("{}\t{}".format(current_activity, abs(current_timestamp - float(timestamp))))
        current_execution_id = None
        current_activity = None
        current_lifecycle_transition = None
        current_timestamp = None
    else:
        current_execution_id = execution_id
        current_activity = activity
        current_lifecycle_transition = lifecycle_transition
        current_timestamp = float(timestamp)
