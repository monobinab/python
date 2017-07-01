#!/usr/bin/env python
_author__ = 'msaha'

import sys
#import datetime
#from __future__ import absolute_import
import os
#from google.cloud import bigquery
#from gcloud import bigquery
import argparse
bigquery_client = gcloud.bigquery.Client()

def memberinfotablecreate(project_id, dataset_id, sql_path):
        client = bigquery.Client(project = project_id)
        print client
        with open(sql_path) as f:
                for line in f:
                        line = line.strip();
                        query = client.run_sync_query(line)
                        query.use_legacy_sql = False
                        query.default_dataset = client.dataset(dataset_id)
                        print dataset_id
                        query.run()

#if __name__ == "__main__":
#       parser = argparse.ArgumentParser(
#               description = __doc__,
#               formatter_class = argparse.RawDescriptionHelpFormatter)
#       parser.add_argument('syw-rts-dev')
#       parser.add_argument('rts_dataset')
#       parser.add_argument('/home/monobina_saha/memberinfotablecreate.sql')
#
#       args = parser.parse_args()
#       #memberinfotablecreate(args.project, args.dataset_id, args.sql_path)
#       memberinfotablecreate(args.project_id, args.dataset_id, args.sql_path)
memberinfotablecreate('syw-rts-dev', 'rts_dataset','/home/monobina_saha/memberinfotablecreate.sql')
