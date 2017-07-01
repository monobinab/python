#!/usr/bin/env python
#this script parses storm log files and creates pipe delilited storm log files
import sys
from datetime import date, timedelta, datetime
#from dateutil import parser

counts = dict()
tmp_lst = list()
# input comes from STDIN (standard input)
for line in sys.stdin:
      client = ""
      try:
          if line is not None and "api: response" in line:
              fields = line.split("|")
              client = fields[3].strip()
              counts[client] = counts.get(client, 0) + 1
      except:
          continue;
    #print('%s' % (counts))
for key, val in counts.items():
       tmp_lst.append((key, val))

for k,v in tmp_lst:
       outline = str(k) + "|" + str(v)
       print('%s' % (outline))

    #print('%s' % (outline))

          #outline = counts


