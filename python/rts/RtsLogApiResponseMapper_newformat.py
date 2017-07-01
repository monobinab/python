#!/usr/bin/env python
#this script create requests
import sys
from os.path import basename
import csv
from pandas import *

# input comes from STDIN (standard input)
for line in sys.stdin:
    if "|" not in line:
        sys.stderr.write("File in old format:" + os.path.basename);
        continue;

        if "api: response" in line:
            #responseFile.write(line);
                        # write the results to STDOUT (standard output);
            print '%s' % (line);
