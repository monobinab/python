#!/usr/bin/env python
#this script create requests
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

    strTokens = line.split("api:");
    if len(strTokens) < 2:
        sys.stderr.write("Error in:" + line);
        continue;

    dateStr = strTokens[0]
    if dateStr is not None:
        dateStr_1 = dateStr.lstrip("PERSIST:") #.replace("2015:","2015|",1)
        n = len(dateStr_1)
        if dateStr_1 is not None and len(dateStr_1) >= 2:
            dateStr_2 = dateStr_1[0:n-2]

    apiStr = strTokens[1];
    if apiStr is not None:
        ind1 = apiStr.rfind(",");
        if ind1 >= 0 and len(apiStr) >= 1:
            apiStr1 = apiStr[0:ind1];
            apiStr2 = apiStr[ind1+1:];

            if apiStr1 is not None:
                ind2=apiStr1.rfind(",");
                if ind2 >= 0 and len(apiStr1) >= 1:
                    apiStr11 = apiStr1[0:ind2];
                    apiStr12 = apiStr1[ind2+1:];

        if apiStr.strip().startswith('response: {"status":"success"'):
            if apiStr11 is not None:
                apiResponseStr = apiStr11.split("time taken:");
                if len(apiResponseStr) >= 2 and apiResponseStr[0] is not None:
                    responseJson=apiResponseStr[0].strip().lstrip("response:").strip();
                    timeTaken=apiResponseStr[1];

                    line = dateStr_2.strip() + "|" + responseJson + "|" + timeTaken.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip() + "\n";
                    #line = dateStr_2.strip() + "|" + apiStr11.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip() + "\n"
                    #responseFile.write(line);
                    # write the results to STDOUT (standard output);
                    print '%s' % (line);
