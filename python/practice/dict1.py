try:
    n = raw_input("enter number: ")
    n = int(n)
    print n
    d = dict()
    for i in range(1, n+1):
        d[i] = i*i
    print d
except:
    print "enter number again"
    quit()
