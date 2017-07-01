__author__ = 'msaha'

#any method with two underscores at beginning and end are special methods
#create a class
class Student(object):
    """Classes can have docstring too just like modules adn functions"""
    def __init__(self, name, id = 20001): # it is like a constructor but actually not. Since it is present right after class is created.
        self.name = name
        self.id = id

#s = Student(args) #s is now an instance of student class. getName() and getSuperclass() are methods used in Java to get metadata information about a class
studentA = Student("Jack")
studentB = Student("Judy", 10005)

print(studentA.name)
print(studentB.id)

#instance variables
class Student:
    def __init__(self, id):
        self.id = id #this is instance variable, separate from id, which was passed into the __init__()
    def setData(self, value):
        self.data = value
    def display(self):
        print(self.data)

#s1 = Student().setData("Jake") #instance object
#s2 = Student()

#print(s1.setData("Jake"))

class MyClassA:
    def setData(self,d):
        self.data = d
    def display(self):
        print(self.data)

a = MyClassA() #these are instances of class MyClassA. This is a namespace that have access to their classes' attributes.
a2 = MyClassA()
a.setData("Python")
a.display()

###############################################################################################

#super class
class MyClassB(MyClassA):
    def display(self):
        print('B: data = "%s"' %self.data) #MyClassB redefines the display of its superclass, and it replaces the display attribute while still inherits the setData method in MyClassA as we see below:

b = MyClassB()
b.setData("BigData")
b.display()
