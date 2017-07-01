
_author__ = 'msaha'
import json
import re
import time
import getpass
import datetime

from __main__ import *

import apache_beam as beam

class requestGroup(beam.DoFn):

        def process(self, context):
            #ors_request_parsed_outFileHandle = open(parameters.parsedMessageFilePath, 'a')
            #ors_request_parsed_outFileHandle = open('/home/monobina_saha/data/output_files/dataflow/ors_parsed_message_datafile.txt')
            #print ors_request_parsed_outFileHandle
            #print lines
            eachLine = context.element
            try:
                strTokens = eachLine.split("start_time")
                data = strTokens[0]
                start_time = strTokens[1]

                output_line = start_date + ":" + data
                yield output_line

            except:
                None;


