""" Write a function to count the vowels in a given string.
these are vowels: a, e, i, o, u """

vowels_in_each_word = {}
sentence = input("Enter A Sentence:\n").split(" ")

def is_vowel(user_input_sentence):

    vowels = ('a', 'e', 'i', 'o', 'u')
    for word_num in range(len(user_input_sentence)):
        vowel_ch = ""
        for ch in user_input_sentence[word_num]:
            if ch in vowels:
                vowel_ch += ch
                vowels_in_each_word[word_num] = vowel_ch



def show_vowels(user_input_sentence):

    for word_num in range(len(user_input_sentence)):
        if word_num in vowels_in_each_word:
            print(f'The word "{user_input_sentence[word_num]}" has {len(vowels_in_each_word[word_num])} vowel(s) which is/are: {vowels_in_each_word[word_num]}')
        else:
            print(f'The word "{user_input_sentence[word_num]}" has no vowels')

is_vowel(sentence)
show_vowels(sentence)