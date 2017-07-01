_author__ = 'msaha'
import json
import re
import time
import getpass
import datetime
from collections import defaultdict

from __main__ import *
import apache_beam as beam

class requestParser(beam.DoFn):

        def process(self, context):
            #ors_request_parsed_outFileHandle = open(parameters.parsedMessageFilePath, 'a')
            #ors_request_parsed_outFileHandle = open('/home/monobina_saha/data/output_files/dataflow/ors_parsed_message_datafile.txt')
            #print ors_request_parsed_outFileHandle
            #print lines
            eachLine = context.element
            try:
                lineJson = ""
                logType = ""
                dataJson = ""
                currentTime = ""
                currentUser = ""
                startTime = ""
                startDate = ""
                startDate1 = ""
                startDate2 = ""
                insertId = ""
                requestStatus = ""
                versionId = ""
                d1 = {}
                lineJson = json.loads(eachLine)
                payloadLinesJson = lineJson['protoPayload']['line']
                versionId = lineJson['protoPayload']['versionId']

                startTime = lineJson['protoPayload']['startTime']
                startDate1 = startTime[:10]
                startDate2 = datetime.datetime.strptime(startDate1, '%Y-%m-%d').date()
                startDate = startDate2.strftime('%Y%m%d')

                insertId = lineJson['insertId']
                requestStatus = lineJson['protoPayload']['status']
                for line in payloadLinesJson:
                    logMessage = line['logMessage']
                    logMessage.encode('utf-8')
                    if "request" in logMessage:
                        #print "request keyword found"
                        logType = "request"
                        dataJson = logMessage.lstrip("request, ").strip()
                        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                        currentUser = getpass.getuser()

                        keys = ['version_id', 'start_time', 'insert_id', 'request_status', 'log_type', 'data_json', 'load_time']
                        values = [str(versionId) + "\t" + str(startTime) + "\t" + str(startDate) + "\t" + str(insertId) + "\t" + str(requestStatus) + "\t" +  str(logType) + "\t"+  str(dataJson) + "\t" + currentTime]
                        values2 = [str(versionId), str(startTime), str(insertId), str(requestStatus), str(logType), str(dataJson), str(currentTime)]
                        outputDictionary = dict(zip(keys, values2))

                        #d1.setdefault(startDate, []).append(outputDictionary)
                        yield outputDictionary

                        #return (values);
                        #yield outputDictionary


            except:
                None;

