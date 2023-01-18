#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    activity = words[0]
    timestamp = words[1]
    lifecycle_transition = words[2]
    execution_id = words[3]
    print("\t{}\t{}\t{}\t{}".format(execution_id, activity, lifecycle_transition, timestamp))
