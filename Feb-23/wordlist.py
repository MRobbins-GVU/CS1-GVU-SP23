# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:12:58 2023

@author: mrobbins
"""

from string import punctuation

def remove_punc(text):
    ''' Remove all punctuation from text and return 
    the rest of the string '''
    # create the accumulator variable
    valid = ""
    
    # go through the entire string letter by letter
    for i in range(len(text)):
        # if the letter is valid, add it to the valid string
        letter = text[i]
        if letter not in punctuation:
            valid += letter
        
    # return the valid string
    return valid

def wordlist(word_list):
    ''' Remove all punctuation from a list of words
    and return the string value. '''
    alpha_string = ''
    for j in range(len(word_list)):
        current_word = word_list[j]
        
        # remove punctuation from the word
        # Or you could do: remove_punc(word_list[j])
        alpha_word = remove_punc(current_word) 
        
        # add the word (with no punc) to the alpha_string
        alpha_string += alpha_word + " "
        
    #return the alpha string
    return alpha_string

def main():
    examples = ["Does this work?", 
                "Um... I think so?",
                "It does! It's working!!! So well!"]

    print(wordlist(examples))
    
main()

