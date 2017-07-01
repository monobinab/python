try:
    inp = raw_input("Enter number: ")
    inp = int(inp)
    for i in range(1, inp):
        o = i * (i - 1)
        if i == 0:
            break
        i = i - 1
    print o
except:
    print "Error, enter number again"
    quit()
