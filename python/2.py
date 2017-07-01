#!/usr/bin/python
import sys, getopt

infile = ''
outfile = ''

myopts, args = getopt.getopt(sys.argv[1:], "i:o:")

for o, a in myopts:
    if o == '-i':
        infile = a
    elif o == '-o':
        outfile = a
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])

print ("Input file: %s and output file: %s" % (infile, outfile))
print infile
print outfile

#for arg in sys.argv:
 #   print (arg[1]);
 #   print (arg[2]);