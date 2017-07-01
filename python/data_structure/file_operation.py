file_name=raw_input('Enter the file name: ')
fhand=open(file_name)
fhand_read=fhand.read() #this will read entire file
print len(fhand_read) # this will give the number of characters in the entire file

for line in fhand:
    if line.startswith('From:'):
        print line  # this will print with an additional new line between each line because print add a new line every time and each line in file has a new line at the end

for line in fhand:
    line = line.rstrip()    #this will eliminate new line
    if line.startswith('From:'):
        print line

count = 0
for line in fhand:
    line = line.rstrip()    #this will eliminate new line
    if not line.startswith('From:'):
        continue
    print line
    count = count + 1

#worked exercise
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line
    line_wanted = line.strip()
    x = line_wanted.find(':')
    confidence = line_wanted[x+1 : ].strip()
    confidence_float = float(confidence)
    sum = sum + confidence_float
    count = count + 1
#print "Sum is : ", sum
#print "Count is: ", count
average = sum/count
print "Average spam confidence:", average
#print "Done"