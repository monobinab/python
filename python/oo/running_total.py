input = raw_input("Enter list input: ")
input_list = input.split(",")
sum = 0


for i in range(len(input_list)):
    sum += input_list[i]
    print sum