hadoop fs -rm -r /output1

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files /nasa_mapper1.py,/nasa_reducer1.py -mapper "python nasa_mapper1.py" -reducer "python nasa_reducer1.py" -input /usr/local/hadoop/405959-event-log/nasa-cev-software-tests-randomized-405959.tsv -output /output1