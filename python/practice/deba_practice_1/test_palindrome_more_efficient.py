user_input = raw_input("Enter palindrome string: ")

isPalindrome = True;

for i in range(len(user_input)/2):
    if user_input[i] != user_input[len(user_input) - i - 1]: # as soon as any character not matching we will break and call it not palindrome
        isPalindrome = False;
        break

if isPalindrome:
    print "palindrome"
else:
    print "not palindrome"