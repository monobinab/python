
input1 = raw_input("enter 1st list: ")
input_list1 = input1.split(" ")

input2 = raw_input("enter 2nd list: ")
input_list2 = input2.split(" ")

def concat_list(list1, list2):
    for item in list2:
        list1.append(item)
    return list1;

print concat_list(input_list1, input_list2)

print input_list1

#concat_list_unlimited = lambda *args: concat(*args)

def concat_list_unlimited(*args):
    for a in args[1:]:
        concat_list(args[0], a)
    return args[0]

input3 = raw_input("enter 2nd list: ")
input_list3 = input3.split(" ")

print "---------------------------------"
print concat_list_unlimited(input_list1)
print "---------------------------------"
print concat_list_unlimited(input_list1, input_list2)
print "---------------------------------"
print concat_list_unlimited(input_list1, input_list2, input_list3)