from collections import Counter

def word_counter(filepath):
    with open(filepath) as file:
        data = file.read()
        word_list = data.split()
        word_count = len(word_list)
        print(f'{word_count} words found in the document')

def char_counter(filepath):
    
    
    with open(filepath) as file:
        data = file.read()
        l_letters = data.lower()
        letters = list(l_letters)
        chars = {}
        chars = dict(letters,0)
        for letters in chars:
            chars[letters] = len(letters)

        print(chars)
