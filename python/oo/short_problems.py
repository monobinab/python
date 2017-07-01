def milestofeet(miles):
    feet = 5280 * miles
    return feet

print milestofeet(13)

def hourstosecs(hours, mins, secs):
    seconds = 60*60*hours + 60*mins + secs
    return seconds

print hourstosecs(7, 21, 37)

def calperimeter(width, length):
    perimeter = 2*width + 2* length
    return perimeter

print calperimeter(4,7)

def calcarea(width, length):
    area = width * length
    return area

print calcarea(4,7)

def calccircumference(radius):
    circumference = 2 * 3.14 * radius
    return circumference

print calccircumference(8)

def calcareaofcircle(radius):
    areaofcircle = 3.14 * (radius)**2
    return areaofcircle

print calcareaofcircle(8)

def calcfuturevalue(principal, interestrate, yrs):
    futurevalue = principal(1 + 0.01*interestrate)**yrs
    return int(futurevalue)

print calcfuturevalue(1000, 7, 10)

def concatstring(string1, string2, string3):
    finalstring = string1 + " " + string2 + " " + string3
    return finalstring

print concatstring("My name is", "Joe", "Warren")

def buildstring(name, age):
    finaloutput = name + " " + "is" + " " + str(age) + " " + "years old"
    return finaloutput

print buildstring("Joe Warren", 52)

import math
def calcdistance(x0, y0, x1, y1):
    distance = math.sqrt((x0 - x1)**2 +(y0 - y1)**2)
    return distance

print calcdistance(2,2,5,6)
