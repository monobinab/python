#!/usr/bin/env python
import math
l=[]
def sq_rt(x):
    C = 50
    H = 30
    Q = math.sqrt ( 2 * C * float(x) ) / H
    return Q

try:
    inp = raw_input("Enter numbers here separated by comma: ")
    inp = inp.split(",")
    for i in inp:
        #print i
        a = sq_rt(i)
        l.append(str(a))
    print ",".join(l)
except:
    print "Error, please enter numbers again"
    quit()
