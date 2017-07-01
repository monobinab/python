import math
#input_number = raw_input("Enter number to check: ")

#this function can only process integer values
def isSquare(num):
    temp = math.sqrt(abs(int(num)))
    #print temp
    if temp.is_integer() == True:
        return True

    else:
        return False
#print isSquare(input_number)
n=0;
i=1;
while(n<20):
    if isSquare(i) == True:
        print i
        n=n+1
    i=i+1