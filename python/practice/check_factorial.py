def factorial(x) :
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

try:
    inp = raw_input("Enter number: ")
    inp = float(inp)
    output = factorial(inp)
    print output
except:
    print "Error"
    quit()
