""" Create a function to check if two strings are anagrams.
An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
using all the original letters exactly once.
For example, the word 'listen' can be rearranged to form the word 'silent'.
"""

anagram_instructions_1 = "Enter word1 to check anagram:\n"
word1 = input(anagram_instructions_1)
print()
anagram_instructions_2 = "Enter word2 to check anagram:\n"
word2 = input(anagram_instructions_1)
print()

def is_anagram(first_word:str, second_word:str):
    if sorted(first_word) == sorted(second_word):
        print(f"Yes {first_word} and {second_word} are anagrams")
    else:
        print(f"No {first_word} and {second_word} are not anagrams")

is_anagram(word1,word2)