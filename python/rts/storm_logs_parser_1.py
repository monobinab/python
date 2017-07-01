#!/usr/bin/env python
#this script create requests
import sys
import datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
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
        fields = line.split(",")

        for field in fields:
            if "LoggingBolt" in field or "PERSIST:" in field:
                # head part
                strTokens = field.split("LoggingBolt")
                if len(strTokens) < 2:
                    sys.stderr.write("Error in:" + line)
                    headDate = ""
                    boltStr = strTokens[0]
                else:
                    runDateStr = strTokens[0]

                    if runDateStr is not None:
                        headDate = runDateStr.rstrip(" a.b")
                    else:
                        headDate = ""

                    boltStr = strTokens[1]

                if boltStr is not None:
                    boltStrTokens = boltStr.split("lid:")

                    if len(boltStrTokens) < 2:
                        sys.stderr.write("Error in:" + boltStr)
                        lid = ""
                    else:
                        lid = boltStrTokens[1].strip()

                    #[INFO] PERSIST: Mon Feb 16 23:37:28 EST 2015: Topology: Changes Scores :
                    boltDateStr = boltStrTokens[0]
                    tailDate = boltDateStr.lstrip("[INFO] PERSIST:").rstrip(": Topology: Changes Scores :")
                    #current_format = "%a %b %d %H:%M:%S %Z %Y"
                    #boltDateStr_2 = datetime.datetime.strptime(boltDateStr_1, current_format);

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
            elif "maxExpiry" in field:
                subFields = field.split(":")
                maxExpiry = subFields[1].strip()
            elif "source" in field:
                subFields = field.split(":")
                source = subFields[1].strip()
            elif "modelId" in field:
                subFields = field.split(":")
                modelId = subFields[1].strip()
            elif "modelId" in field:
                subFields = field.split(":")
                modelId = subFields[1].strip()

    line = headDate + "|" + tailDate + "|" + lid + "|" + modelId + "|" + oldScore + "|" + newScore + "|" + minExpiry + "|" + maxExpiry + "|" + source

    print('%s' % (line))
