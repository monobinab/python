#palindrome ignoring white space, dot (only considering alphabetic character)
#string reverse
#string normalization (get a dirty string , return a clean string. Normal form - one has a extrac space, dots, capitals, '_)
#string concatenation (algorithm, not with +)
#list of string as input, create unique tokens
#substring
#instring (find a sequence of characters within a string e.g. "is" exist and which location) - how can you communicate two things - return -1 if not found,if found return positive location
#write a function how to return multiple information in a structure/class
#implementation of to_upper , to_lower, to_camelcase, to_change_case
#hash of a string(hash is to find a similarity)


#check palindrome (a string is palindrome if it is same forward and backward)
def if_palindrome(s):
    i = 0;
    j = len(s) - 1;
    while(i<=j):
        if s[i].lower() != s[j].lower():
             return False;
        i += 1;
        j -= 1;
    return True;

print(if_palindrome("tenEt"))

#print out string
def str_print(s):
    new_s = "";
    for i in range(len(s)):
        print(s[i])
        new_s = new_s + s[i];
    return new_s;

print(str_print("abcde"))

#reverse string
def str_reverse(s):
    j = len(s) - 1;
    new_s = ""
    while (j>=0):
        new_s = new_s + s[j]
        j -= 1 ;
    return new_s;

print(str_reverse("abcde"))

#string normalization
def str_normal(s):
    i=0;
    j = len(s) - 1;
    print(s)
    print (j)
    new_s = "";
    while (i<=j):
        if s[i].isalpha() or s[i].isnum():
            new_s = new_s + s[i].lower();
            print(i)
        j -= 1;
        i += 1;
    return new_s;

print(str_normal("aDnnmnklkdfer_.90"))

#string concatenation algorithm.
#TODO This doesn't produce correct result
def str_concat(str1, str2):
    i = 0
    j= len(str1) -1 ;
    k = 0
    l = len(str2) -1;
    new_s = ""
    while (i<=j):
        new_s = new_s + str1[i]
        i += 1;
        j -= 1;
    new_s
    while (k<=l):
        new_s = new_s + str2[k]
        k += 1;
        l -= 1;
    return new_s;

print(str_concat("cat", "dog"))


#string concatenation algorithm
def str_concat1(str1, str2):
    i = 0
    j= len(str1) -1 ;
    k = 0
    l = len(str2) - 1 ;
    new_s = ""
    for i in range(len(str1)):
        new_s = new_s + str1[i]
    new_s
    for j in range(len(str2)):
        new_s = new_s + str2[j]

    return new_s;

print(str_concat1("cat", "dog"))

#find substring between position 4 and 6
def create_substring(input_string):
    i = 0
    new_str = ""
    for i in range(len(input_string)):
        if 4<=i<=6:
            new_str = new_str + input_string[i]
        else:
            continue;
    return new_str

print(create_substring("abcdefghi"))

#in string operation to find if a string exists and which location
#TODO
def instring(main_string, pattern):
    i = 0;
    j = 0;
    beg_index = 0
    end_index = 0
    for i in range(len(main_string)):
        if main_string[i].lower() == pattern[0].lower():

            for j in range(len(pattern)):
                beg_index = main_string[i]
    return (True, i);
    return False;

print(instring("abcdefg", "bqr"))

#string hashing
def hash(string):
    import hashlib;
    #print(hashlib.algorithms_available); #to check available algorithms
    #print(hashlib.algorithms_guaranteed);
    hashString = hashlib.md5(string.encode())
    return hashString.digest()

print(hash("monobina"))

#practical problem password check
import uuid
import hashlib
def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

print(hash_password("monobina"))

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(":")
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

#new_pass = input("Please enter password: ")
#hashed_password = hash_password(new_pass)
#print("The string to store in the db is: " + hashed_password)
#old_pass = input("Now please confirm password: ")
#if check_password(hashed_password, old_pass):
#    print("You entered correct password")
#else:
#    print("I am sorry password didn't match")


#capitalize one word
def capitalize(s):
    return s[0].upper() + s[1:]
print(capitalize("monobina"))

#capitalize multiple words
def capitalize_1(s):
    str_tokens = s.split(" ")
    output_str = ""
    for str_token in str_tokens:
        str_token = str_token[0].upper() + str_token[1:] + " "
        output_str += str_token
    return output_str

print(capitalize("monobina saha"))

print("monobina saha".capitalize()) #capitalize function only capitalizes first letter of a sentence

#change case by creating a new string
def changeCase(s):
    output_str = ""
    for i in range(len(s)):
        if s[i].islower():

            output_str += s[i].upper()
        else:
            output_str += s[i].lower()
    return output_str

print(changeCase("mOnoBina iS"))

#change case of original string
def changeCase1(s):
    for i in range(len(s)):
        if s[i].islower():
            s[i].upper()
        else:
            s[i].lower
    return s

print(changeCase1("monoBiNa"))

def changeCase2(s):
    for i in range(len(s)):
        if s[i].islower():
            s[i] = s[i].upper()
    return s

#print(changeCase2("moNoBina"))

import string
def changeCaseChar(char):

    if char in string.ascii_uppercase:
        return char.lower()
    else:
        return char.upper()

print(changeCaseChar("moNobIa"))










