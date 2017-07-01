file_in = '/Users/msaha/PycharmProjects/data/vibes_parsed_output.txt'
infile_hand = open(file_in, 'r')
file_out = '/Users/msaha/PycharmProjects/data/appended_line_no.txt'
outfile_hand = open(file_out, 'w')
line_count = 0

for line in infile_hand:
    try:
        new_line = line + "|" + str(line_count) + "\n"


        outfile_hand.write(new_line)
        line_count=line_count + 1

    except:
        raise;