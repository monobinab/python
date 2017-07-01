__author__ = 'msaha'
import json
import unicodedata
import sys

#inFile = '/Users/msaha/PycharmProjects/gcp/data/infiles/ors-request.txt'
inFile = str(sys.argv[1])
print inFile
inFileHandle = open(inFile, 'r')

#outFile = '/Users/msaha/PycharmProjects/gcp/data/outfiles/parsed_ors-request.txt'
outFile = str(sys.argv[2])
print outFile
outFileHandle = open(outFile, 'w')

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






