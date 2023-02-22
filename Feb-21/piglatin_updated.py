# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 18:37:59 2023

@author: Robbins
"""

def pig_latin(word):
    """ Translates the given word into pig latin """ 

    vowels = "aeiouAEIOU"
    first_letter = word[0]
    second_letter = word[1]
    
    # Option 1: Word starts with a consonant and a vowel
    if first_letter.upper() not in "AEIOU" and second_letter.upper() in "AEIOU":
        partial_word = word[1:]
        return partial_word + first_letter + "ay"
    
    # Option 2: Word starts with two consonants
    if first_letter not in vowels and second_letter not in vowels:
        partial_word = word[2:]
        return partial_word + first_letter + second_letter + "ay"
    
    # Option 3: Word starts with a vowel  
    if word[0] in vowels:
        return word + "way"
    
def main():
    print(pig_latin("Melissa"))
    print(pig_latin("Cheese"))
    print(pig_latin("Opossum"))
    
main()