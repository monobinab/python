#Write a function that returns the elements on odd positions in a list.
input = raw_input("Enter ")
input_list=input.split()
n=len(input_list)
i=0
output_list=list()

#this also works
def odd_elements(input_list):
    for i in range(n):
        if i%2 == 0:
            output_list.append(input_list[i])
        #print output_list
    return(output_list)

#print odd_elements(input_list)

#deba
def odd_elements_alt(input_list):
    for i in range(0, n, 2):
        output_list.append(input_list[i])
        #print output_list
    return(output_list)

print odd_elements_alt(input_list)