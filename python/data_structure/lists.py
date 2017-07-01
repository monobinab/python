friends = ['Joseph', 'Glenn', 'Sally']
#for loop like strings.
for friend in friends :
    print 'Happy New Year:', friend

for i in range(len(friends)) :
    friend = friends[i]
    print 'happy New Year:', friend # the two ways produce same output

#sort method is used to sort list
friends.sort()

a=[1,2,3]
b=[4,5,6]
c=a+b
print c
#[1,2,3,4,5,6]

#we can slice it like strings
t = [1, 2, 13, 14, 12, 7]
t[1:3]
#[2,13]
t[:4]
#[1, 2, 13, 14]
t[:]
#[1, 2, 13, 14, 12, 7]

#some methods: append, pop, remove

#we can build a list with append
stuff = list()
stuff.append('book')
stuff.append('99')
print stuff
#['book', 99]

print 'book' in stuff

len(stuff), max(stuff), min(stuff), sum(stuff), sum(stuff)/len(stuff)

#when you use string you can do in this way
total = 0
count = 0
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count +1

average = total/count
print average

#when you use list, you can do this way. This is another way which can be used when you are using list
numlist = []
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print'Average:', average

#split used in string operation creates a list of words
#if you have a list, just use for loop to loop through the words in the list
stuff = ['with', 'three', 'words']
for w in stuff:
    print w

--------------------------------------------------------------------------------------------------------------
#worked exercise
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

#file-

#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    fields = line.split()
    for field in fields:
        if field in lst: continue;
        lst.append(field)


lst.sort()
print lst

#from exercise of course era
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count = 0
fh = open(fname)
for line in fh:

    if line.startswith("From "):
        fields = line.split(" ")
        field2 = fields[1].strip()
        count = count + 1
        print field2
print "There were", count, "lines in the file with From as the first word"






