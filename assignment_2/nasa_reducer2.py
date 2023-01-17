#!/usr/bin/env python3
import sys

current_activity = None
current_duration_average = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    activity, duration = line.split("\t")
    if current_activity is not None:
        assert current_activity == activity
        current_duration_average = (current_duration_average * current_count + float(duration)) / (current_count + 1)
        current_count += 1
    else:
        current_activity = activity
        current_duration_average = float(duration)
        current_count = 1