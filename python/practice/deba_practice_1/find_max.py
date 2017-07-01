def find_max(x,y):
    x = float(x)
    y = float(y)
    if x > y :
        return(x)
    else:
        return(y)

a=raw_input("Input first number: ")
b=raw_input("Input second number: ")
print find_max(a,b)
