""" Write a function to count the vowels in a given string.
these are vowels: a, e, i, o, u """

vowels_in_each_word = {}
sentence = input("Enter A Sentence:\n").split(" ")

def is_vowel(string):

    vowels = ('a', 'e', 'i', 'o', 'u')
    for word_num in range(len(string)):
        vowel_ch = ""
        for vowel in vowels:

            if vowel in string[word_num]:
                vowel_ch += vowel
                vowels_in_each_word[word_num] = vowel_ch


def show_vowels(string):

    for word_num in range(len(string)):
        if word_num in vowels_in_each_word:
            print(f'The word "{string[word_num]}" has {len(vowels_in_each_word[word_num])} vowel(s) which are: {vowels_in_each_word[word_num]}')
        else:
            print(f'The word "{string[word_num]}" has no vowels')

is_vowel(sentence)
show_vowels(sentence)
