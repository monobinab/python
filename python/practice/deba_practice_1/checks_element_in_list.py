#Write a function that checks whether an element occurs in a list.
input=raw_input("enter a list: ")

input_list=input.split()
search_value=raw_input("Enter search value: ")


def check_element(list, x):
     if x in input_list:
         return(True)
     else:
         return(False)

print check_element(input_list, search_value)
