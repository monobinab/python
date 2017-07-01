#!/usr/bin/python
import commands
import sys

input_file = sys.argv[1];
input_file_handle = open(input_file, 'r');

for line in input_file_handle:
        print line;
        commands.getoutput('bq query --use_legacy_sql=false line')