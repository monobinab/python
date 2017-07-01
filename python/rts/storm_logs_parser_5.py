#!/usr/bin/env python
#this script parses storm log files and creates pipe delilited storm log files
import sys
from datetime import date, timedelta, datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
  try:
    head = ""
    headDate = ""
    lid = ""
    tailDate = ""
    modelId = ""
    oldScore = ""
    newScore = ""
    minExpiry= ""
    maxExpiry = ""
    source = ""

    if line is not None:
      if ": source:" in line:
        line.replace(': source:', '\, source:')

        fields = line.split(",")

        for field in fields:
            if "LoggingBolt" in field or "PERSIST:" in field:
                # head part
                strTokens = field.split("LoggingBolt")
                if len(strTokens) < 2:
                   # sys.stderr.write("Error in:" + line)
                    headDate = ""
                    boltStr = strTokens[0]
                else:
                    runDateStr = strTokens[0]

                    if runDateStr is not None:
                        headDate = runDateStr.rstrip(" a.b")
            #current_headDateFormat = "%a %b %d %H:%M:%S %Z %Y"
                        #headDate_1 = datetime.datetime.strptime(headDate, current_headDateFormat);
                    else:
                        headDate = ""

                    boltStr = strTokens[1]

                if boltStr is not None:
                    boltStrTokens = boltStr.split("lid:")

                    if len(boltStrTokens) < 2:
                       # sys.stderr.write("Error in:" + boltStr)
                        lid = ""
                    else:
                        lid = boltStrTokens[1].strip()

                    #[INFO] PERSIST: Mon Feb 16 23:37:28 EST 2015: Topology: Changes Scores :
                    boltDateStr = boltStrTokens[0]
                    tailDate_1 = boltDateStr.lstrip("PERSIST").rstrip(": Topology: Changes Scores :")
                    ind1 = tailDate_1.find(":")
                    if ind1 >= 0 and len(boltDateStr) >= 1:
                        tailDate = tailDate_1[ind1+1:].strip()
                        current_tailDateFormat = "%a %b %d %H:%M:%S %Z %Y"
                        tailDate_2 = datetime.strptime(tailDate, current_tailDateFormat);


            elif "modelId" in field:
                subFields = field.split(":")
                modelId = subFields[1].strip()
            elif "oldScore" in field:
                subFields = field.split(":")
                oldScore = subFields[1].strip()
            elif "newScore" in field:
                subFields = field.split(":")
                newScore = subFields[1].strip()
            elif "minExpiry" in field:
                subFields = field.split(":")
                minExpiry = subFields[1].strip()
                current_minExpiry_format = "%m/%d/%Y"
                minExpiry_1 = datetime.strptime(minExpiry, current_minExpiry_format)
            elif "maxExpiry" in field:
                subFields = field.split(":")
                maxExpiry = subFields[1].strip()
                current_maxExpiry_format = "%m/%d/%Y"
                maxExpiry_1 = datetime.strptime(maxExpiry, current_maxExpiry_format)
            elif "source" in field:
                subFields = field.split(":")
                source = subFields[1].strip()


    outputline = headDate + "|" + str(tailDate_2) + "|" + lid + "|" + modelId + "|" + oldScore + "|" + newScore + "|" + str(minExpiry_1) + "|" + str(maxExpiry_1) + "|" + source

    print('%s' % (outputline))
  except:
    #do noting   
    #continue
    print('%s' % ("error:"+line))
