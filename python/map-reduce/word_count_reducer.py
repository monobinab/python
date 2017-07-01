#!/usr/bin/env python
import sys
in_file = '/Users/msaha/PycharmProjects/map-reduce/data/example_word_count_mapper_outfile.txt'
infile_hand = open(in_file, 'r')
out_file = '/Users/msaha/PycharmProjects/map-reduce/data/example_out_reduce_file.txt'
out_hand = open(out_file, 'w')

last_key = None
running_total = 0

for input_line in infile_hand:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)
    value = float(value)
    if last_key == this_key:
        running_total +=value
    else:
        if last_key:
            print("{0}\t{1}".format(last_key, running_total))
        running_total = value
        last_key = this_key

#if last_key == this_key:
    out_hand.write("{0}\t{1}".format(last_key, running_total))