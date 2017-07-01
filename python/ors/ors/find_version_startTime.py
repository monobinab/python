_author__ = 'msaha'
import json
import unicodedata
import sys
import os
import glob

def find_versionId(input_location):
	with open(input_location, 'r') as f:
        	
                	lineJson = ""
                	versionId = ""
                	first_line = f.readline()
                	lineJson = json.loads(first_line)
                	versionId = lineJson['protoPayload']['versionId']
			return(versionId)
       
def find_startDate(input_location):
        with open(input_location, 'r') as f:
                        lineJson = ""
                        startTime = ""
                        first_line = f.readline()
                        lineJson = json.loads(first_line)
                        startTime = lineJson['protoPayload']['startTime']
                        startDate = startTime[:10]
                        return(startDate) 
