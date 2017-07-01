#!/usr/bin/env python
#this script create requests
import sys

# input comes from STDIN (standard input)
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
            line = dateStr_2.strip() + "|" + apiStr11.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip();
		    #requestFile.write(line)
            # write the results to STDOUT (standard output);
            print '%s' % (line);