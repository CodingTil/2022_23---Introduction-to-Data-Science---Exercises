#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    case = words[0]
    activity = words[1]
    timestamp = words[2]
    lifecycle_transition = words[3]
    execution_id = words[4]
    print(f"\t{execution_id}\t{activity}\t{lifecycle_transition}\t{timestamp}")