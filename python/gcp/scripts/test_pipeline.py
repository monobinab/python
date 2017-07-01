from __future__ import absolute_import

import logging
import apache_beam as beam
from apache_beam.utils.options import PipelineOptions
from apache_beam.utils.options import SetupOptions
from oauth2client.client import GoogleCredentials
#from apiclient.discovery import build
import httplib2
#import google.cloud.dataflow as df

from parser_dataflow import requestParser
from group import requestGroup
import datetime


def run(argv=None):
    p = beam.Pipeline() #todo set option
    lines = p | beam.io.Read('ReadFromText', beam.io.TextFileSource('gs://ms_orslogs/input/ors_request_consumed_datafile.txt'))
    parsed_lines = lines | beam.ParDo(requestParser())

    parsed_lines | 'parsewrite' >> beam.io.Write(beam.io.TextFileSink('gs://ms_orslogs/output/ors_request_parsed_datafile.txt'))

    #keys = ['version_id', 'start_time', 'insert_id', 'request_status', 'log_type', 'data_json', 'load_time']
    #values = parsed_lines
    #keyValueLines = beam.Map(lambda (keys, values): (keys, values))

    #keyed_lines = parsed_lines | beam.ParDo(requestGroup())
    #keyed_lines = parsed_lines | 'keyedlines' >> beam.io.Write(beam.io.TextFileSink('gs://ms_orslogs/output/ors_request_keyed_datafile.txt'))
    #group = parsed_lines | beam.GroupByKey()

    #group | 'groupwrite' >> beam.io.Write(beam.io.TextFileSink('gs://ms_orslogs/output/ors_request_grouped_datafile.txt'))


    schema = 'version_id:STRING, start_time:STRING, insert_id:STRING, request_status:STRING, log_type:STRING, data_json:STRING, load_time:STRING'

    parsed_lines | beam.io.Write('Write', beam.io.BigQuerySink(
        'syw-ors-qa:ors_logs.ors_client_requests_partitioned',
        schema=schema,
        write_disposition = beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        create_disposition = beam.io.BigQueryDisposition.CREATE_IF_NEEDED))





    p.run()

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()