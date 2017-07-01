input_str = raw_input("Enter list of numbers: ")
input_list = input_str.split(",")

sum = 0
i=0
for i in input_list:
    sum += float(i)
    print sum

print "-------------------------------"

def sumofnumbers(total, input_list, n=len(input_list)):
    """
    This function takes a list as an input and computes running total
    """
    #total = 0
    #total = float(total);
    print "initial total=", total
    i = 0
    while i < n:
        num = input_list[i]
        total += float(input_list[i])
        i = i + 1
        #print num
        print total

def simpleSum(a,b):
    return a+b;

sumofnumbers(sum, input_list)
print "-------------------------------"
sumofnumbers(2000.0, input_list, 3)

print "-------------------------------"
sumofnumbers(simpleSum(23,23), input_list, 3) #example of calling one function from another function