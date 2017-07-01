__author__ = 'msaha'
_author__ = 'msaha'
import json
import unicodedata
import sys
import os
import glob
import pickle
inFile = '/home/monobina_saha/data/input_files/row_json.json'
#inPath = str(sys.argv[1])
print(inFile)
#inFileHandle = open(inFile, 'r')
inFileHandle = open(inFile, 'r')
outFileDir = '/home/monobina_saha/data/output_files/'
outFileBasename = 'issuance_log.txt'
outFilePath = outFileDir + outFileBasename
print outFilePath
outFileHandle = open(outFilePath, 'w')
with open(inFile, 'r+') as f:
    for eachLine in inFileHandle:
        try:
            lineJson = ""
            logMessage = ""
            issueType = ""
            memberId = ""
            issueTime = ""
            offerType = ""
            offerCd = ""
            productGrp = ""
            productSubGrp = ""
            numberOfOffers = ""
            maxCatalinaOffers = ""
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
                    productGrp = vars[5].strip()
                    productSubGrp = vars[6].strip()
                    numberOfOffers = vars[7].strip()
                    maxCatalinaOffers = vars[8].strip()
                    #outputLine = "{" + "\"" + "log_type" +  "\"" + ":" + "\"" + str(issueType) + "\"" + "," + "\"" + "member_id" + "\"" + ":"  + str(memberId) + "," + "\"" + "issue_time" + "\"" + ":" + "\"" + issueTime + "\"" + "," + "\"" + "offer_type" + "\"" + ":" + "\"" + offerType + "\"" + "," + "\""
+ "offer_code" + "\"" + ":" + "\"" + offerCd + "\"" + "," + "\"" + "product_group" + "\"" + ":" + "\"" + productGrp + "\"" + "," + "\"" + "product_subgroup" + "\"" + ":" + "\"" + productSubGrp + "\"" + "," + "\"" + "number_of_offers" + "\"" + ":" +  numberOfOffers  + "," + "\"" + "max_catalina_offers" + "\
"" + ":"  + maxCatalinaOffers + "}" + "\n"
                    keys = ['log_type', 'member_id', 'issue_time', 'offer_type', 'offer_code', 'product_group', 'product_subgroup', 'number_of_offers', 'max_catalina_offers']
                    values = [issueType, memberId, issueTime, offerType, offerCd, productGrp, productSubGrp, numberOfOffers, maxCatalinaOffers]
                    outputDictionary = dict(zip(keys, values))
                    outputDictionary = outputDictionary
                    print type(outputDictionary)
                    print (outputDictionary)
                    f.seek(0)
                    #outFileHandle.write(keys, values)
                    #pickle.dump(outputDictionary, outFileHandle)
                    #json_output = json.dumps(outputDictionary) #this dumps entire thing in one line
                    json.dump(outputDictionary, outFileHandle) #this dumps each json in multiple lines
                    #outFileHandle.write(json_output)
                    outFileHandle.write('\n')
        except:
            outFileHandle.close(); raise;
            #continue
outFileHandle.close()