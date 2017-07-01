#!/usr/bin/env python
#this script create requests
import sys
from datetime import date, timedelta, datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
  try:
   date_Str = ""
   error_message = ""
   member_id = ""
   client = ""

   if line is not None:
    fields = line.split("|")

    for field in fields:
     if "api" in field or "PERSIST" in field:
         subFields = field.split(":")
         date_Str = subFields[1].lstrip("PERSIST:").rstrip(: api: response)
         current_format = " %a %b %d %H:%M:%S %Z %Y"
         date_Str = datetime.strptime(dateStr, current_format)
     elif "errorCode" in fields:
         error_message = field.strip()
     elif member_id = field.strip()
     elif client = field.strip()

   outputline = str(date_Str) + "|" + str(error_message) + "|" + str(member_id) + "|" + str(client)

   print('%s' % (outputline))
  except:
    #do noting
    continue;


























        strTokens=field.split(": api: response");
        if len(strTokens) < 2:
            dateStr = ""
            errorCode = strTokens[0]
        else:

            dateStr=strTokens[0]
            if dateStr is not None:
              dateStr_1=dateStr.lstrip("PERSIST:").strip() #.replace("2015:","2015|",1)
              n= len(dateStr_1)
              if datestr_1 is not None and len(dateStr_1) >= 2:
                dateStr_2=dateStr_1[0:n-2]
                current_format = " %a %b %d %H:%M:%S %Z %Y"
                dateStr_3 = datetime.strptime(dateStr_2, current_format)

            apiStr=strTokens[1];
            if apiStr is not None:
              ind1=apiStr.rfind(",");
              if ind1 >= 0 and len(apiStr) >= 1:
                  apiStr1 = apiStr[0:ind1];
                  errorCode = apiStr1.lstrip
            apiStr1=apiStr[0:ind1];

            ind2=apiStr1.rfind(",");
            apiStr11=apiStr1[0:ind2];
            apiStr12=apiStr1[ind2+1:];


            apiStr2=apiStr[ind1+1:];

    #TODO: check for nulls
    if apiStr.strip().startswith('response: {"errorCode":'):
            line = dateStr_2.strip() + "|" + apiStr11.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip() + "\n"
            errorFile.write(line);
            #line = dateStr_2.strip() + "|" + apiStr11.strip() + "|" + apiStr12.strip() + "|" + apiStr2.strip() + "\n"
            #responseFile.write(line);
            # write the results to STDOUT (standard output);
            print '%s' % (line);