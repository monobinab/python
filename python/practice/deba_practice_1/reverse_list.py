input = raw_input("Enter input numbers: ")
input_list = input.split()
i=0
def reverse_input(input_list):
    for i in range(len(input_list)-1):
        field1 = input_list[i]
        field2 = input_list[i+1]
        temp=field2
        input_list[i+1] = input_list[i]
        input_list[i] = temp
        i=i+1
    return(input_list)

print reverse_input(input_list)

