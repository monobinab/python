#when we encounter a new name we need to add the new entry into dictionary and if this is the second or later time we have seen the name, we simply add one to the count in the dictionary
counts=dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print counts

print counts.get(name,0)

if name in counts:
    print counts[name]
else:
    print 0

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts

#how to find which word occurs most in a line
#python reads the line in a file as string
#splits the string into list of strings
#create a dictionary and calculate total number of occurances of each word

counts = dict()
print 'Enter a line of text:'
line = raw_input('')
words = line.split()
print 'Words:', words
print 'Counting...'
for word in words:
    counts[word] = counts.get(word,0) + 1

print 'Counts:', counts


#we can go through a dictionary and look at the values of the keys
counts = {'chuck' : 1 , 'fred' : 42 , 'jan':100}
for key in counts:
    print key, counts[key]

#retrieving lists of keys and values
jjj = {'chuck':1, 'fred':42, 'jan':100}
print list(jjj)  # this only gives the keys
print jjj.keys()
print jjj.values() #these jjj.keys() and jjj.values() return the list of values in order
print jjj.items() # this returns tuples

#two iteration variables
jjj = {'chuck':1, 'fred':42, 'jan':100}
for aaa,bbb in jjj.items():
    print aaa, bbb

#read and file and print out the word that occurs most number of times
name = raw_input("Enter the name of the file: ")
handle = open(name, 'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1

bigCount = None
bigWord = None

for word, counts in counts.items():
    if bigCount is None or counts > bigCount:
        bigWord = word
        bigCount = counts
print bigWord, bigCount

###############################################################################################
#exercise
#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')
counts = dict()
sender = ""

for line in handle:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        if sender not in counts:
            counts[sender] = 1
        else:
            counts[sender] = counts[sender] + 1
#print counts

bigCount = None
bigWord = None
for sender, counts in counts.items():
    if bigCount is None or counts > bigCount:
        bigWord = sender
        bigCount = counts
print bigWord, bigCount

#######################################################################################################
