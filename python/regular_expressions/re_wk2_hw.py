import re;
infile = '/Users/msaha/PycharmProjects/regular_expressions/actual_data_wk2.txt'
infile_hand = open(infile)
numlist = list()
num =0

for line in infile_hand:
    line.strip()
    #print line
    stuff = re.findall('([0-9]+)', line)
    if not len(stuff) > 0: continue
    #print stuff;
    #loop the list to sum all the number
    for i in stuff:
        numlist.append(i)
        #print numlist
        num = num + int(i);

#print len(numlist)
print num