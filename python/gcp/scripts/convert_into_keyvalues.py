__author__ = 'msaha'
from parser_dataflow import *

from __main__ import *
import apache_beam as beam

class keyValueConverter(beam.DoFn):

        def process(self, context):

            eachLine = context.element
            try:
                keys = ['version_id', 'start_time', 'insert_id', 'request_status', 'log_type', 'data_json', 'load_time']
                #values = [str(versionId) , str(startTime) , str(insertId) , str(requestStatus), str(logType) , str(dataJson) , currentTime]
                outputDictionary = dict(zip(keys, eachLine))
                return (outputDictionary);

            except:
                return();


