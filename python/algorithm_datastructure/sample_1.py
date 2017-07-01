__author__ = 'msaha'
#source site
#http://www.bogotobogo.com/python/python_interview_questions_2.php#print-dir
#Write a function f()
#Q: We have the following code with unknown function f(). In f(), we do not want to use return, instead, we may want to use generator.
#for x in f(5):
#    print x,

#The output looks like this:
#0 1 8 27 64

def cube_function(n):
    for x in range(n):
        yield x**3
    return x**3

def cube_function_1(n):
    return [x**3 for x in range(n)]

print (range(5))
print(cube_function_1(5))

#################################################################################
#prints output if a number is primes function
#output should be 2 3 5 7 11 ... 83 89 97
def isPrime(n):
    if n == 1:
        return False
    for t in range(2, n) :
        #print("this is input", n)
        #print("this is t", t)
        if n % t == 0:
            return False
    return True

#for n in primes():
 #   print(n)

def primes(n=1):
    while n < 100:
        if isPrime(n) :
            #yield n
            print ("this is prime", n)
        n = n + 1

primes()
#####################################################################################
#what is __init__.py

####################################################################################
#Build a string with the numbers from 0 to 100, "0123456789101112..."
a = ""
n = 0
def numstring(n=0):
    a = ""

    while n < 100:

        a = a + str(n)

        n = n + 1
    return (a)

print (range(100))
print(numstring())

##################################################################################
#How can we get home directory using '~' in Python?

import os
print (os.path.expanduser('~'))

###################################################################################
#os.path.dirname() & os.path.basename()

import os
file = '~/PycharmProjects/algorith_datastructure/sample_1.py'
directory = os.path.dirname(file)
print (directory)
filename = os.path.basename(file)
print (filename)
print(os.getcwd())
####################################################################################

#range vs. xrange
print(range(5))
#print(xrange(1,5))  #xrange is discontinued in newer version of python and replaced with range

###############################################################################

def docstring(arg):
    """I am a docstring at the beginning of the function"""
    return (arg)

print (docstring(1))
print(docstring)
print(docstring.__doc__)

#####################################################################
#monkey patching. Sneaking in to change the code dynamically. It is used in testing.
class MyClass:
    def f(selfself):
        print ("f()")

def monkey_f(self):
    print("monkey_f()")

MyClass.f = monkey_f
obj = MyClass()
obj.f()

########################################################
#lambda function
#It is anonymous function which is not bound to a name. It uses a construct called lambda.
#this is usual way
def func(x): return x ** 3
print (func(5))

#this is lambda way. Lambda always returns something. It doesn't contain return statement. Lambdas are simpler than def because it is limited to an expression.
lamb = lambda x: x** 3
print(lamb(5))

def f(x,y,z): return x+y+z
print(f(2, 3,4))

f = lambda x, y, z : x + y + z
print(f(2, 3, 4))

############################################################################
#Making a list with unique element from a list with duplicate elements
#this didn't work
dup_list = [1, 2, 3, 4, 4, 4, 5, 6, 1, 2, 7, 8, 9, 10]
unique_list = []
def create_unique_list(dup_list):
    for i in dup_list:
        temp = dup_list[i]
        print (temp)
        print (dup_list[i])
        if temp != unique_list[i:]:
            unique_list.append(dup_list[i])
        else:
            continue;
        return (unique_list)

#print (create_unique_list(dup_list))

#remove duplicates
def remove_duplicates(dup_list):
    output = []
    seen = set()
    for value in dup_list:
        if value not in seen:
            output.append(value)
            seen.add(value)
            #print(output)
            #print(seen)
    return (output)
print(remove_duplicates(dup_list))

unique_list = list(set(dup_list)) #set is a function used to make a set that is unique and convert it back to list
print (unique_list)
print(type(unique_list))
print(type(dup_list))

#############################################################################
def print_all(*args):
    for x in enumerate(args): #enumerate creates a counter to an iterable
        print(x)

print_all('A', 'b', 'b', 'a')

elements = ('elem1', 'elem2', 'elem3', 'elem4')
for elem in elements:
    print (elem)

for count, elem in enumerate(elements):
    print (count, elem)


for elem in enumerate(elements):
    print(elem)

#############################################################################
def kargs_function(**kargs): #kargs for keyword arguments is a name=value syntax
    for k,v in kargs.items():
        print (k,v)

kargs_function(**{'uno':'one', 'dos':'two', 'tres':'three'})

###############################################################################

#immutable -objects that cannot be changed after created
#immutable -> tuple, str, int, float, frozen
#mutable -> list, set, dict, byte array

############################################################################
# difference between remove, del, pop on lists

#remove() function removes teh first matching value, not a specific index

a = [5, 6, 7, 7,8]
a.remove(7)
print(a)

#pop() and del() removes by index
a = [5, 6, 7, 7,8]
a.pop(1)
print(a)

a = [5, 6, 7, 7,8]
del a[1]
print(a)

#########################################################################
#Given a list of string, ['Black', 'holes', 'are', 'where', 'God', 'divided', 'by', 'zero'], print each word in a new line:
s = ['Black', 'holes', 'are', 'where', 'God', 'divided', 'by', 'zero']
print('\n'.join(s))

for elem in s:
    print(elem)

##########################################################################
integers = [ x for x in range(11)]
print (integers)
filter_list = list(filter(lambda x: x % 2 == 0, integers)) #filter function calls our lambda function for each element of the list and rturns a new list that contains only those elements
print(filter_list)
map_list = list(map(lambda x: x**2, integers)) #map() is called for each element in the list and it creates a new list which contains return values from lambda function
print (map_list)
from functools import reduce
sum = reduce(lambda x, y: x + y, integers) #reduce needs at least 2 args. the function is called for first 2 elements, then the result of that call and the third element ad so on. IT is called for n-1 times if the list contains n elements
print(sum)

integers = (x for x in range(11))
print (integers)

#########################################################################

#print a list of file in dir
import os

def file_list(dir):
    basedir = dir
    subdir_list = []
    for item in os.listdir(dir):
        fullpath = os.path.join(basedir,item)
        if os.path.isdir(fullpath):
            subdir_list.append(fullpath)
        else:
            print (fullpath)

    for d in subdir_list:
        file_list(d)

#file_list('/dir')
##############################################################################################














