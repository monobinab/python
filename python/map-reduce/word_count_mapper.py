#!/usr/bin/env python
import sys
in_file = '/Users/msaha/PycharmProjects/map-reduce/data/example_datafile.txt'
infile_hand = open(in_file, 'r')
out_file = '/Users/msaha/PycharmProjects/map-reduce/data/example_word_count_mapper_outfile.txt'
out_hand = open(out_file, 'w')


for line in infile_hand:
    line = line.strip() # strip is method associated with string data type, it strips the carriage return by default
    keys = line.split() # split line at blanks by default and returns list
    for key in keys:
        value = 1
        out_hand.write('{0}\t{1}'.format(key, value)) # the {} is replaced by the 0th, 1st items in format list


