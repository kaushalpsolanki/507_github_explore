import random


vowels = ['a', 'e', 'i', 'o', 'u']

def num_vowels(input):
    num_vowels = 0
    for i in input:
        if i in vowels:
            num_vowels += 1
    return num_vowels


print(num_vowels("hello"))
