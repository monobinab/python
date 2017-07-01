from os import walk
dirpath = /incoming/rts/flume
dirnames = Jan/2015
filenames = jboss*

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    hadoop jar /opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.2.jar -files RtsLogApiResponseMapper.py  -mapper RtsLogApiResponseMapper.py -reducer org.apache.hadoop.mapred.lib.IdentityReducer -input dirpath/dirnames/filenames -output /user/msaha/rts/incoming_response
    break

indir = hadoop fs -ls /incoming/rts/flume/Jan/2015
infile = jboss*
outfile = /auto/home/msaha/rts/incoming_response

--determine a timestamp and pickup all the files that are greater than old timestamp and less than equal to current timestamp
--process your files using one or multiple processes
--after processing is done current timestamp as last timestamp for the next process
