#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line = line.strip()
    activity, duration = line.split("\t")
    print("{}\t{}".format(activity, duration))
