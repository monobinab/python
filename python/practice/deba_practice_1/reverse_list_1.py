#by declaring an output list and then populating the output list.
# This is good if the list is not huge because we are creating another list and memory usage is more.
# But it needs one for loop instead of two because reading from the end of the input list and populating from the beginning of the output list.

input=raw_input("Enter list: ")
input_list=input.split()
n=len(input_list)
output_list=list();
for i in range(n):
    print input_list[n-1-i]
    output_list.append(input_list[n-1-i]);
print output_list
