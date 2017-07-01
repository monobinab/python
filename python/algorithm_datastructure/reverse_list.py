__author__ = 'msaha'

x = [];
y = [];

#by creating another new list
def reverse_list(x):
    l = len(x);
    y = [];
    for i in range(l):
        #print("lth element of the original list is", + x[l-1]);
        y.append(x[l-1-i]);#taking length -1 because of the way python indexing works. -i so that indexing advances as i increases in each iteration

    return y;

x = [1, 2, 3, 4, 5];
print(x);
print (reverse_list(x));

#working on the same list. Have to split the list into two for swapping.
def reverse_list_efficient(input_list):
    l = len(input_list);
    print("split length of list", l/2)
    print("split length remainder: ", l%2)
    if l%2 == 0:  #calculation will be different if the list contains even or odd number of elements. That's why checking that first and setting number of iterations.
        iterations = round(l/2);
    else:
        iterations = round(l/2);
    print ("iterations is", iterations);
    for i in range(iterations):
        print (i)
        temp = input_list[l-1-i];
        print(temp);
        input_list[l-1-i] = input_list[i];
        print(input_list);
        input_list[i] = temp;

    return input_list;

input_list=[1, 2, 3, 4, 5];
print(reverse_list_efficient(input_list))





