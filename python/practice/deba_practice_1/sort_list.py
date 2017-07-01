input = raw_input("enter input list: ")
input_list = input.split()

def sort_list(input_list):
    for n in range(len(input_list)-1): # we will loop until 1 less because we are comparing using pair of two. Here the whole list if getting sorted from semi sorted inside loop.
        for i in range(len(input_list)-1-n): # here we are using two values each time to compare
            field1=float(input_list[i])
            field2=float(input_list[i+1])
            if field2<field1:
                temp=input_list[i+1]
                input_list[i+1]=input_list[i]
                input_list[i]=temp

    return(input_list)

print sort_list(input_list)