__author__ = 'msaha'

def sort_list(input_list):
    l = len(input_list);

    print("length is", l);
    for j in range(l-1):
        for i in range(l-1):
            if input_list[i] > input_list[i+1]:
                print(input_list[i]);
                print(input_list[i+1]);
                temp = input_list[i] ;
                input_list[i] = input_list[i+1];
                input_list[i+1] = temp;
                print (input_list);
    return input_list;

even_input_list = [3, 4,6,5,1, 9];
print(sort_list(even_input_list));

odd_input_list = [3, 4,6,5,1];
print(sort_list(odd_input_list));

already_sorted_list = [1,2,3,4,5]
print(sort_list(already_sorted_list))

totally_unsorted_list = [9,8,7,6,5,4,3,2,1];
print(sort_list(totally_unsorted_list))

