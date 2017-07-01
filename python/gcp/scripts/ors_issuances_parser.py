__author__ = 'msaha'
import json
import unicodedata
import sys
import os
import glob

inFile = '/Users/msaha/PycharmProjects/gcp/data/infiles/00:00:00_00:59:59_A0:1461546000.json'

#inPath = str(sys.argv[1])
print(inFile)
inFileHandle = open(inFile, 'r')

for eachLine in inFileHandle:

    try:
        lineJson = ""
        startTime = ""
        versionId = ""
        lineJson = json.loads(eachLine)
        startTime = lineJson['protoPayload']['startTime']
        versionId = lineJson['protoPayload']['versionId']
        print(startTime)


        outFileBasename = 'issuance_log' + '_' + str(versionId) + '_' + str(startTime) + '.txt'
        print(outFileBasename)
    except:
        break;
inFileHandle.close()

inFile = '/Users/msaha/PycharmProjects/gcp/data/infiles/00:00:00_00:59:59_A0:1461546000.json'
print(inFile)
inFileHandle = open(inFile, 'r')

#outFileDir = '/Users/msaha/PycharmProjects/gcp/data/outfiles/'
#outFile = str(sys.argv[2])
outFile = str("'" + outFileBasename  + "'")
#outFile = str(outFileDir + outFileBasename)
print(outFile)
outFileHandle = open("'" + outFile + "'" , 'w')

for eachLine in inFileHandle:

        try:
            lineJson = ""
            logMessage = ""
            issueType = ""
            memberId = ""
            issueTime = ""
            offerType = ""
            offerCd = ""
            bu = ""
            field7 = ""
            field8 = ""
            field9 = ""

            lineJson = json.loads(eachLine)
            payloadLinesJson = lineJson['protoPayload']['line']
            for line in payloadLinesJson:
                logMessage = line['logMessage']
                logMessage.encode('utf-8')
                if "issuance" in logMessage:
                    vars = logMessage.split(",")
                    issueType = vars[0].strip()
                    memberId = vars[1].strip()
                    issueTime = vars[2].strip()
                    offerType = vars[3].strip()
                    offerCd = vars[4].strip()
                    bu = vars[5].strip()
                    field7 = vars[6].strip()
                    field8 = vars[7].strip()
                    field9 = vars[8].strip()
                    outputLine = issueType + "|" + memberId + "|" + issueTime + "|" + offerType + "|" + offerCd + "|" + bu + "|" + field7 + "|" + field8 + "|" + field9 + "\n"

                    outFileHandle.write(outputLine)
        except:
            outFileHandle.close(); raise;
            continue

outFileHandle.close()






