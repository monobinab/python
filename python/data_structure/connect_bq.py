__author__ = 'msaha'

import httplib2
import sys
import json
#import bigquery
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.file import Storage
from oauth2client.client import GoogleCredentials
from oauth2client import GOOGLE_TOKEN_URI
#from oauth2client.tools import run
# REPLACE WITH YOUR Project ID
PROJECT_NUMBER = 'syw-ors-1226'
# REPLACE WITH THE SERVICE ACCOUNT EMAIL FROM GOOGLE DEV CONSOLE
SERVICE_ACCOUNT_EMAIL = 'monobina-saha@syw-ors-1226.iam.gserviceaccount.com'
from OpenSSL import SSL
from OpenSSL import crypto
#p12 = crypto.load_pkcs12(file("push.p12", 'rb').read(), "987Dora123")
# OBTAIN THE KEY FROM THE GOOGLE APIs CONSOLE
# More instructions here: http://goo.gl/w0YA0
#f = open('privatekey.p12', 'rb')
#key = f.read()
#f.close()
#credentials = SignedJwtAssertionCredentials(
#    SERVICE_ACCOUNT_EMAIL,
#    key,
#    scope='https://www.googleapis.com/auth/bigquery')
credentials = GoogleCredentials.get_application_default()
http = httplib2.Http()
http = credentials.authorize(http)
service = build('bigquery', 'v2')
datasets = service.datasets()
response = datasets.list(projectId=PROJECT_NUMBER).execute(http)
#print 'Dataset list:'
#for dataset in response['datasets']:
#  print '%s' % dataset['datasetReference']['datasetId']
tables = service.tables()
response = tables.list(projectId=PROJECT_NUMBER, datasetId='ors_requestlog').execute(http)
print response
dictlist = []
temp = []
for key, value in response.iteritems():
    temp = [key,value]
    dictlist.append(temp)
    #print dictlist

print type(response)
tablelist = []
print 'Tables list:'
for table in response['tables']:
        table = table['tableReference']['tableId']
        print table
        tablelist.append(table)
print type(tablelist)
print '%s' % tablelist
tablename = 'ors_request_log_20160518'
if tablename in tablelist:
        print ('response = 1')
else:
        print ('response = 0')
