fruit='banana'
count = 0
for letter in fruit:
    print letter
    if letter == 'a':
        count = count + 1
print count;

print('n' in fruit)

print type(fruit)
print dir(fruit) # it gives you list of functions that you can use with string

#Common string functions:
#str.capitalize  #this capitalizes the first character
#str.endswith()
#str.find()  # fruit.find('na')
#str.lower()

new_fruit = fruit.replace('banana', 'mango')
print new_fruit

#below is a parsing data example
line = 'from monobina.saha@searshc.com Sat Sept 11 09:13:14'
atpos = line.find('@')
print atpos
sppos = line.find(' ', atpos)
print sppos
web_address = line[atpos+1 : sppos]
print web_address