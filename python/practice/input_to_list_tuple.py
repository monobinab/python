try:
    inp = raw_input("Enter list of numbers here separated by comma: ")
    l = inp.split(",")
    t = tuple(l)
    print l
    print t
except:
    print "Error, couldn't convert to list or tuple"
    quit()
