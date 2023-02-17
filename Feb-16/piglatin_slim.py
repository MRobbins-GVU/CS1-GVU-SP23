# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 18:37:59 2023

@author: Robbins
"""

def pig_latin(word):
    """ Translates the given word into pig latin """ 

    vowels = "aeiouAEIOU"
    # Option 1: Word starts with a consonant and a vowel
    if word[0] not in vowels and word[1] in vowels:
        return word[1:] + word[0] + "ay"
    
    # Option 2: Word starts with two consonants
    if word[0] not in vowels and word[1] not in vowels:
        return word[2:] + word[0:2] + "ay"
    
    # Option 3: Word starts with a vowel
    if word[0] in vowels:
        return word + "way"
    
def main():
    print(pig_latin("Melissa"))
    print(pig_latin("Cheese"))
    print(pig_latin("Opossum"))
    
main()