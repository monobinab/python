^ beginning of line
$ end of line
. matches any character
* repeats zero or more number of times
+ repeats one or more number of times
\s matches whitespace
\S matches any non-white space character
*? repeats zero or more times, non greedy
+? repeats one or more times, non-greedy
[aeiou] matches a single character in the listed set
[^XYZ] matches characters not in listed set
[a-z0-9] the set of characters can include a range
( indicates where string extraction starts
) indicates where string extraction ends




import re
#re.search is similar to find
#re.findall()
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
#  e.g. ^X-\S+: means starts with X- followed by any one or more non blank character.

x = "My 2 favorite numbers are 9 and 152"
y = re.findall('[0-9]+', x) #give me a python list that matches this condition
['2', '9', '152']
y = re.findall('[AEIOU]+', x)
x = 'From: Using the : character'
y = re.findall('^F.+:', x)   #the repeat character + or * is greedy, goes as much outward as possible
print y
['From: Using the :']
y = re.findall('^F.?+:', x)

###############################################
x = 'From stephen.marquet@yahoo.com Sat Jan 07 1989'
y = re.findall('\S+@\S+', x)
print y
stephen.marquet@yahoo.com

#to make it more specific. To find only lines that start with From
y = re.findall('From ()')
#to find the last part of email address after '@' sign
y = re.findall('^From .*@([^ ]*)', x)

##################################################
# to read from a file and process the file
infile = 'mbox-short.txt'
infile_hand = open(infile, r)
numlist = list()

for line in infile_hand:
    line = line.rstrip()
    stuff = re.findall('^X-Dspam Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue;
    num = float(stuff[0])
    numlist.append(num)

print ('Maximum: ', max(numlist))

#######################################################
#\ escape character
import re
x = 'We just received $10.00 as reward'
y = re.findall('\$[0-9.]+', x)  # [0-9]. means a digit or a period
print y
['$10.00']

#######################################################
