"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def is_valid_format(word_format):
    for i in word_format:
        if i != "c" and i != "v":
            return True
    return False

def main():
    word_format = input("Sequence: ")
    while is_valid_format(word_format):
        word_format = input("Sequence: ")

    word = ""
    for kind in word_format.lower():
        if kind in "c%":
            word += random.choice(CONSONANTS)
        elif kind in "v#":
            word += random.choice(VOWELS)

    print(word)

main()