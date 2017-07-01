input = raw_input("Enter a list of numbers: ")

print input


#list_length=len(input_list)
#no_of_iterations = (list_length)
i=0
j=0
temp=0
max = 0

#this didn't work
def find_max_from_list_bk(input_list):

    for i in range(no_of_iterations):
            field1 = input_list[i]
            print field1
            field2 = input_list[i+1]
            print field2
            if float(field1) > float(field2):
                max = float(field1)
                temp = float(field2)
                field2 = field1
                field1 = temp
                return(max)




#this worked
def find_max_from_list(input):
    input_list = input.split()
    max=float(input_list[0])
    i=0
    for i in range(len(input_list)):

        if float(input_list[i]) > max:
            max = float(input_list[i])

    return(max)

print find_max_from_list(input)
