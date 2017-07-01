d = {'a' : 10, 'b' : 1, 'c' : 22}
t = d.items()
t
[('a', 10), ('c', 22), ('b', 1)]
t.sort()
t
[('a', 10), ('b', 1), ('c', 22)]

t = sorted(d.items())
for k,v in sorted(d.items()) :
    print k,v

#############################################################################################################
#if we want to find 5 most common words in a document then we have to sort by the values not the keys. This is the simple way of doing histogram of word frequency count

c = {'a' : 10, 'b' : 1, 'c' : 22}
tmp = list()
for k, v in c.items() :
    tmp.append((v,k)) # two brackets to indicate (v,k) is a single argument, which is a tuple

print tmp
[(10, 'a'), (22, 'c'), (1, 'b')]
tmp.sort(reverse=True)
print tmp
[(22, 'c'), (10, 'a'), (1, 'b')]

#10 most common words
file = ('sample_text_file.txt')
fhand = open(file, 'r')
count = dict()

for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

print count
count1 = list()
for key, val in count.items(): #this will create a list of two tuples as each element
    count1.append((val, key))
print count1

count1.sort(reverse=True)
#count2_1 = count2[:10]
for k, v in count1[:10]:
    print v,k
###########################################################################################################

c = {'a' : 10, 'b' : 1, 'c' : 22}

print sorted([(v,k) for k,v in c.items()])

##########################################################################################################

#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name, 'r')
count = dict()
tmp_lst = list()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        mailtime = words[5]
        #print mailtime
        timeStrTokens = mailtime.split(":")
        mail_hour = timeStrTokens[0]
        #print mail_hour
        count[mail_hour] = count.get(mail_hour, 0) + 1 #output: {'09': 2, '18': 1, '16': 4, '15': 2, '14': 1, '11': 6, '10': 3, '07': 1, '06': 1, '04': 3, '19': 1, '17': 2}

#print count
for key, val in count.items():
    tmp_lst.append((key,val))
#print "1"
#print tmp_lst
tmp_lst.sort()
#print "2"
#print tmp_lst  # this will print as list of tuples like [('04', 3), ('06', 1), ('07', 1), ('09', 2), ('10', 3), ('11', 6), ('14', 1), ('15', 2), ('16', 4), ('17', 2), ('18', 1), ('19', 1)]

for k,v in tmp_lst:
    print k,v

#final output
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1