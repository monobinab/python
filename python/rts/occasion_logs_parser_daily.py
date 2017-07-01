#!/usr/bin/env python
# this script parses storm log files and creates pipe delilited occasions log files
import sys
from datetime import date, timedelta, datetime
# from dateutil import parser

# input comes from STDIN (standard input)
for line in sys.stdin:
    try:
        headDate = ""
        persistDate = ""
        topology = ""
        lid = ""
        eid = ""
        custEvent = ""
        successFlag = ""
        tag = ""
        purchaseOccasion = ""

        if line is not None and "OccasionResponses" in line:
            fields = line.split(",")

            for field in fields:
                if "OccasionResponses" in field:
                    # head part
                    strTokens = field.split("OccasionResponses")
                    if len(strTokens) < 2:
                        # sys.stderr.write("Error in:" + line)
                        headDate = ""
                        OccasionStr = strTokens[0]
                    else:
                        headDateStr = strTokens[0]
                        headDate = headDateStr.rstrip("a.u.d")
                        #current_headDateFormat = "%a %b %d %H:%M:%S %Z %Y"
                        #headDate_1 = datetime.datetime.strptime(headDate, current_headDateFormat);
                        #if datetime.strptime(headDate_1, '%Y-%m-%d %H:%M:%S') < datetime.combine((date.today()-timedelta(days=3)), datetime.min.time()):
                        #  continue;
                        OccasionStr = strTokens[1]

                        if OccasionStr is not None:
                            OccasionStrTokens = OccasionStr.split(": Topology:")
                            if len(OccasionStrTokens) < 2:
                            # sys.stderr.write("Error in:" + boltStr)
                                persistDate = ""
                                TopologyStr = OccasionStrTokens[0].strip()
                            else:
                                persistDateStr = OccasionStrTokens[0]
                                persistDate = persistDateStr.lstrip("Dao [INFO] PERSIST: ").rstrip()
                                TopologyStr = OccasionStrTokens[1].strip()

                                if TopologyStr is not None:
                                    TopologyStrTokens = TopologyStr.split(": lid:")
                                    if len(TopologyStrTokens) < 2:
                                       topology = ""
                                       lid = TopologyStrTokens[0].strip()
                                    else:
                                       topology = TopologyStrTokens[0].strip()
                                       lid = TopologyStrTokens[1].strip()


                elif "eid" in field:
                    subFields = field.split(":")
                    eid = subFields[1].strip()
                elif "custEvent" in field:
                    subFields = field.split(":")
                    custEvent = subFields[1].strip()
                elif "successFlag" in field:
                    subFields = field.split(":")
                    successFlag = subFields[1].strip()
                elif "tag" in field:
                    subFields = field.split(":")
                    tag = subFields[1].strip()
                elif "purchaseOccasion" in field:
                    subFields = field.split(":")
                    purchaseOccasion = subFields[1].strip()

        outputline = headDate + "|" + persistDate + "|" + topology + "|" + lid + "|" + eid + "|" + custEvent + "|" + successFlag + "|" + tag + "|" + purchaseOccasion
        # print('%s' % (line))
        print('%s' % (outputline))
    except:
        #do nothing
        continue;
        #raise;
        #print('%s' % ("error:"+line))
