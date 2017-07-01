import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print line

###############################################
#achieve above not using regular expression
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >=0:
        print line
#################################################
# to instruct that 'From' appears in beginning of line
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') >=0:
        print line
####################################################
#to instruct same in re
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print line
#################################################
#  . represents wildcard
#  * represents any number of times
#  \S represents any non blank character
#  e.g. ^X-\S+: means starts with X- followed by any non blank character and then :