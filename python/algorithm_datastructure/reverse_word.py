__author__ = 'msaha'

def reverse_word(input_words):
    word_list = input_words.split(" ");
    l = len(word_list);
    print(l);
    if l%2 == 0:  #calculation will be different if the list contains even or odd number of elements. That's why checking that first and setting number of iterations.
        iterations = round(l/2);
        print(iterations)
    else:
        iterations = round(l/2);
        print(iterations)
    for i in range(iterations):
        temp = word_list[l-1-i];
        word_list[l-1-i] = word_list[i];
        word_list[i] = temp;
        print (word_list)
    input_words = str(word_list)
    return input_words;

input_words = "I am a human"
print(reverse_word(input_words))

