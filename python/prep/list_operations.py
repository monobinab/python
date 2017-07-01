#find a element in the element(binary search, linear search etc)
#sorting a list e.g. quick sort, merge sort etc
#reverse order
#concatenate two lists - return a new list
#sublist - based on certain conditions. Conditions may be location or by searching and return 5 elements
#loop the list and print out.Print out in pyramid way





# some functions to work with loop
def find_max(data):
    biggest = data[0];
    print(biggest)
    for val in data:
        if val > biggest:
            biggest = val;
    return biggest;


print(find_max([1000, 1, 2, 3, 7, 7, 100, 4]))


def find_min(data):
    smallest = data[0];
    for val in data:
        if val < smallest:
            smallest = val;
    return smallest;


print(find_min([0, 2, -3, 9]))


# for loop usign index
def find_max_index(data):
    max_index = 0;
    for i in range(len(data)):
        if data[i] > data[max_index]:
            max_index = i;
    return max_index;


print(find_max_index([-100, 1, 2, 3, 6, 7]))


# checks if a value exist
def if_exist(data, target):
    print(data)
    print(target)
    found = False;
    for val in data:
        if val == target:
            found = True;
            break;
    return found;


print(if_exist("abcde", "a"))
print(if_exist([0, 1, 2, 3, 4, 5], 2))

#this doesn't work yet
# sort
def sort_list(data):
    i = 0;
    # j = 1;
    # temp = 0;
    for i in range(len(data) - 1):
        temp = 0;
        for j in range(len(data)):
         print("data1 is", data[i])
        #  print(data[j])
         if data[i] > data[i + 1]:
            data[i] = temp;
            print("data[i] is ", data[i]);
            print("temp is ", temp)
            data[i] = data[i + 1];
            data[i + 1] = temp
            i = i + 1
            # j = j+1
        else:
            continue;
    return data;


#print(sort_list([3, 2, 8, 6, 9, 0, 11]))

#create a list with values from odd number index
def odd_index_finder(data):
    result = [];
    for i in range(len(data)):
        if i%2 == 0:

            result.append(data[i]);

    return result;

print(odd_index_finder([0, 1, 2, 3, 4, 5,6]))

#create list by eliminating certain values
def filter_list(data, target_value):
    i = 0
    for val in data:
        print(val)
        if val == target_value:
            i = data[val]
            data.pop(i);
    return data;

print(filter_list([1, 2, 6, 3, 8], 2))



