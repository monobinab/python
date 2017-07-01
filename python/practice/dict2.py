def square_dict(x):
    d=dict()
    d[x] = x*x
    return d[x]

a= square_dict(9)
print a

try:
    n = raw_input("enter number: ")
    n = int(n)
    for i in range(1, n+1):
        d[i] = square_dict(i)
    print d
except:
    print "enter number again"
    quit()
