# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:08:01 2023

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
            print(valid)
        
    # return the valid string
    return valid

def main():
    gnarly_text = "Hello!!!!!@#$%^(&^%#$$@#$^@$&( I AM @#"
    gnarly_text += "!#$^ SO !#%#$^! HAPPY."
    print(remove_punc(gnarly_text))
    
    
main()