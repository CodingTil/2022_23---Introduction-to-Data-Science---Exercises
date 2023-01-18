hadoop fs -rm -r /output2

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files /nasa_mapper2.py,/nasa_reducer2.py -mapper "python nasa_mapper2.py" -reducer "python nasa_reducer2.py" -input /output1/part-00000 -output /output2