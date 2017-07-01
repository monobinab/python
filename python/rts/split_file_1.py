#!/usr/bin/env python
#this script create requests
import sys

# HOW TO RUN
#localfile e.g., 1421954986971_sample.txt
# cat 1421954986971_sample.txt | python <>.py

#original hdfs File /incoming/rts/flume/Jan/2015/jboss-.1421954986971
#hadoop fs -cat /incoming/rts/flume/Jan/2015/jboss-.1421954986971 | python <>.py

#output file handlers
requestFile = open('requestfile.txt', 'w')
responseFile = open('responsefile.txt', 'w')
errorFile = open('errorfile.txt', 'w')

for line in sys.stdin:
    strTokens=line.split("api:");
    dateStr=strTokens[0]
    dateStr_1=dateStr.lstrip("PERSIST:") #.replace("2015:","2015|",1)
    n=len(dateStr_1)
    dateStr_2=dateStr_1[0:n-2]

    apiStr=strTokens[1];

    ind1=apiStr.rfind(",");

    apiStr1=apiStr[0:ind1];

    ind2=apiStr1.rfind(",");
    apiStr11=apiStr1[0:ind2];
    apiStr12=apiStr1[ind2+1:];

    apiStr2=apiStr[ind1+1:];

    #TODO: check for nulls
    if apiStr.strip().startswith("Incoming Request"):
        line = dateStr_2.strip() + "|" + apiStr11.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip() + "\n";
        requestFile.write(line);
    elif apiStr.strip().startswith('response: {"errorCode":'):
        line = dateStr_2.strip() + "|" + apiStr11.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip() + "\n"
        errorFile.write(line);
    else:
        apiResponseStr=apiStr11.split("time taken:");
        responseJson=apiResponseStr[0].strip().lstrip("response:").strip();
        timeTaken=apiResponseStr[1];
        line = dateStr_2.strip() + "|" + responseJson + "|" + timeTaken.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip() + "\n";
        #line = dateStr_2.strip() + "|" + apiStr11.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip() + "\n"
        responseFile.write(line);
