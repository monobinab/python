#!/usr/python/env

input_file = '/Users/msaha/PycharmProjects/data/vibes_parsed_output.txt'
output_file = '/Users/msaha/PycharmProjects/data/new_add.txt'
input_fhand = open(input_file, 'r')
output_fhand = open(output_file, 'w')

for line in input_fhand:
    if line is not None:
        try:
            #strTokens = line.split("|")
            new_line = line + "|" + "newfield" + "\n"

            output_fhand.write(new_line)
        except:
            raise;




