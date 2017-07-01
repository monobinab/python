#!/usr/bin/env python
#this script parses storm log files and creates pipe delilited storm log files
import sys
from datetime import date, timedelta, datetime
#from dateutil import parser

counts = dict()
tmp_lst = list()
# input comes from STDIN (standard input)
for line in sys.stdin:
      source = ""
      if line is not None:
          fields = line.split(",")
          for field in fields:
              if "source" in field:
                  subFields = field.split(":")
                  source = subFields[1].strip()
                  counts[source] = counts.get(source, 0) + 1


      for key, val in counts.items():
          tmp_lst.append((key, val))

      for k,v in tmp_lst:
          outline = str(k) + "|" + str(val)



      #outline = counts
print('%s' % (counts))



