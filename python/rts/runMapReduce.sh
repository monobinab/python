#!/bin/bash

#/opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p0.3/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.3.0-mr1-cdh5.1.2.jar
#/opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p0.3/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar
#/opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p0.3/lib/hadoop-mapreduce/hadoop-streaming.jar
#/opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.3.0-mr1-cdh5.1.2.jar
#/opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar
#/opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-mapreduce/hadoop-streaming.jar



hadoop jar /opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.2.jar \
-files RtsLogApiRequestMapper.py  -mapper RtsLogApiRequestMapper.py \
-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
-input /incoming/rts/flume/Jan/2015/jboss-.1421954986971 \
-output /user/msaha/rts_api_request_jan2015_1421954986971

hadoop jar /opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.2.jar \
-files RtsLogApiResponseMapper.py  -mapper RtsLogApiResponseMapper.py \
-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
-input /incoming/rts/flume/Jan/2015/jboss-.1421954986973 \
-output /user/msaha/rts_api_response_jan2015_1421954986973

hadoop jar /opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.2.jar \
-files RtsLogApiCallErrorMapper.py  -mapper RtsLogApiCallErrorMapper.py \
-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
-input /incoming/rts/flume/Jan/2015/jboss-.1421954986971 \
-output /user/msaha/rts_api_call_error_jan2015_1421954986971

hadoop jar /opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.2.jar \
-files do_not_run_RtsLogApiResponseMapper.py  -mapper do_not_run_RtsLogApiResponseMapper.py \
-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
-input /incoming/rts/flume/Jan/2015/jboss-* \
-output /smith/rts/Jan/2015/

hadoop jar /opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.2.jar \
-files storm_logs_parser_2.py  -mapper storm_logs_parser_2.py \
-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
-input /incoming/rts/flume/Jan/2015/storm-* \
-output /smith/rts/storm/Jan/2015/

hadoop jar /opt/cloudera/parcels/CDH-5.1.2-1.cdh5.1.2.p470.103/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.2.jar \
-files storm_logs_parser_3.py -mapper storm_logs_parser_3.py \
-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
-input /incoming/rts/flume/Feb/2015/storm-.*[0-9] \
-output /smith/rts/storm/Feb/2015