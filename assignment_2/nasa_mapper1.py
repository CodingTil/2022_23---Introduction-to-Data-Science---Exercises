#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line = line.strip()
    activity, timestamp, lifecycle_transition, execution_id = line.split("\t")
    print("{}\t{}\t{}\t{}".format(execution_id, lifecycle_transition, activity, timestamp))
