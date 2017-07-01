user_input = raw_input("Enter palindrome string: ")


for letter in user_input:
    print letter

for i in range(len(user_input)/2):
    str1 = ""
    str2 = ""
    str1 = str1 + user_input[i]

    str2 = str2 + user_input[len(user_input) - i - 1]

if str1 == str2:
    True
    print "palindrome"
else:
    False
    print "not palindrome"

