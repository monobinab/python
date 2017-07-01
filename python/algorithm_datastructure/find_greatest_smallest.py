__author__ = 'msaha'

def find_greatest(input_list):
    l = len(input_list);
    for j in range(l -1):
        for i in range(l-1):
            if input_list[i] > input_list[i+1]:
                temp = input_list[i+1];
                input_list[i+1] = input_list[i];
                input_list[i] = temp;
    return input_list[l-1]

input_list = [5,4, 3,8, 0, 1]
print("greatest number is", find_greatest(input_list))


def find_smallest(input_list):
    l = len(input_list);
    for j in range(l -1):
        for i in range(l-1):
            if input_list[i] > input_list[i+1]:
                temp = input_list[i+1];
                input_list[i+1] = input_list[i];
                input_list[i] = temp;
    return input_list[1]

input_list = [5,4, 3,8, 0, 1]
print("smallest number is", find_smallest(input_list))
