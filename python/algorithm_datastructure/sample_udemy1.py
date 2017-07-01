__author__ = 'msaha'

def sum1(n):
    final_sum = 0

    for x in range(n+1):   #iteratively add it
        final_sum += x

    return final_sum

print(sum1(10))

def sum2(n):
    final_sum = 0
    final_sum = (n*(n+1))/2  #is a different algorithm
    return final_sum

print(sum2(10))

#%timeit sum1(100) #timeit module is used to objectively understand efficiency about how long it takes and how many loops it makes (how much cpu/memory intensive)
#%timeit sum2(100)


#Big O notation how much run time will grow relative to the increase in input

#1 - constant
#e.g. of O(1) constant
def func_constant(values):
    print (values[0])

lst = [1, 2, 3]
func_constant(lst)

#log(n) - logarithmic
#n - linear
#e.g of O(n) linear
def func_lin(lst):
    for val in lst:
        print (val)  #print each element of the list at a time
func_lin(lst)

def func_lin1(lst):
    print (lst)  #prints as list

func_lin1(lst)

# print 1 time
def print_once(lst):
    for val in lst:
        print (val)

print_once(lst)

def print_2(lst):   #linear and printing it two times like union
    for val in lst:
        print(val)

    for val in lst:
        print(val)
print_2(lst)

#nlog(n) - log linear
#n^2 - quadratic  O(n^2) quadratic
def func_quad(lst):
    for item_1 in lst:
        for item_2 in lst:
            print (item_1, item_2)

func_quad(lst)
#n^3 - cubic
#2^n - exponential

def comp(lst):
    print (lst[0])  #O(1)
    ###O(1/2*n)
    midpoint = int(len(lst)/2)  #len returns float, so converting it into int
    print(midpoint)
    for val in lst[:midpoint]:
        print (val)

    for x in range(10): #O(10)
        #print (x)
        print("hello world")
lst = [1,2,3,4,5,6,7,8,9,10]
comp(lst)

#total BigO for this entire loop
#O(1 + n/2 + 10)
#if the n is very big value close to infinity, it boils down to O(n) because 1 and 10 are insignificant at that time

# check if a number is in list
def matcher(lst, match):
    for item in lst:
        if item == match:
            return True

    return False
print(matcher(lst,1))  #O(1) is the best case where you loop once
print(matcher(lst, 11)) #worst case when it doesn't exist in the list. you have to loop through the entire list n times

#create a list with the word "new" as many number of times as you specify
def create_list(word, x):  #O(n) linear in terms of memory complexity
    new_list = []
    for num in range(x):
        new_list.append(word)
    print (new_list)

create_list('new', 5)

def printer(n):
    for x in range(10): #Time Complexity 0(n)
        print("Hello World") #Space Complexity O(1)

printer(10)

def list_method1():
    lst = []
    for x in range(1000):
        lst = lst + [x]
    print(lst)

list_method1()
