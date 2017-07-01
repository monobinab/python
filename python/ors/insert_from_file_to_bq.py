__author__ = 'msaha'
import sys
import os
import json
import httplib2
import sys
import datetime
#from oauth2client.contrib import appengine
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.file import Storage
from oauth2client.client import GoogleCredentials
_SCOPE = 'https://www.googleapis.com/auth/bigquery'
from oauth2client import GOOGLE_TOKEN_URI
from find_version_startTime import *
versionId = find_versionId('/home/monobina_saha/data/input_files/row_json.json')
print(versionId)
startDate = find_startDate('/home/monobina_saha/data/input_files/row_json.json')
startDate1 = datetime.datetime.strptime(startDate, '%Y-%m-%d').date()
startDate2 = startDate1.strftime('%Y%m%d')
PROJECT_NUMBER = 'syw-ors-1226'
SERVICE_ACCOUNT_EMAIL = 'monobina-saha@syw-ors-1226.iam.gserviceaccount.com'
DATASET_ID = 'ors_requestlog'
TABLE_ID = 'ors_request_log'
inFile = '/home/monobina_saha/data/output_files/issuance_log.txt'
inFileHandle = open(inFile, 'r')
templateSuffix = '_v' + versionId + '_' + startDate2
print(templateSuffix)
today = datetime.date.today()
today = today.strftime('%Y%m%d')
print today
if startDate2 < today:
        print("it is older data")
else:
        print("it is current data")
credentials = GoogleCredentials.get_application_default()
http = httplib2.Http()
http = credentials.authorize(http)
bigquery = build('bigquery', 'v2', credentials=credentials)
service = build('bigquery', 'v2')
datasets = service.datasets()
response = datasets.list(projectId=PROJECT_NUMBER).execute(http)
tables = service.tables()
response = tables.list(projectId=PROJECT_NUMBER, datasetId='ors_requestlog').execute(http)
tablelist = []
print 'Tables list:'

for table in response['tables']:
        table = table['tableReference']['tableId']
        print table
        tablelist.append(table)
print type(tablelist)
print '%s' % tablelist
tablename = TABLE_ID + templateSuffix
print tablename
if tablename in tablelist:
        print ("table exists")
        for row in inFileHandle:
                row = json.loads(row)
                body = {
                        "rows":[{"json":row}]
                        }
                response = bigquery.tabledata().insertAll(
                projectId=PROJECT_NUMBER,
                datasetId=DATASET_ID,
                tableId=TABLE_ID ,
                body=body).execute()
                print response
else:
        print("new table will be created")
        for row in inFileHandle:
                row = json.loads(row)
                body = {
                        "templateSuffix": templateSuffix,
                        "rows":[{"json":row}]
                        }
                response = bigquery.tabledata().insertAll(
                projectId=PROJECT_NUMBER,
                datasetId=DATASET_ID,
                tableId=TABLE_ID ,
                body=body).execute()
                print response
