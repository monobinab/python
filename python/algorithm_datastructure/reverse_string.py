__author__ = 'msaha'

word = "dora"
word_list = list(word)

def reverse_word(word):
    word_list = list(word);
    l_word = len(word_list);
    print(l_word);
    if l_word%2 == 0:
        iterations = round(l_word/2);
        print(iterations)
    else:
        iterations = round(l_word/2);
        print(iterations)
    for i in range(iterations):
        temp = word_list[i];
        word_list[i] = word_list[l_word-1-i];
        word_list[l_word-1-i] = temp;
    word = str(word_list)
    return word

word = "dorai"
print (reverse_word(word))