# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 18:07:39 2023

@author: Robbins
"""

def main():
    str1 = "Hello world!"
    str2 = "I love cats!"
    str3 = "Ready for the weekend."
    
    print(str1, str2, str3)

    print("Hell" in str1) # expecting True    
    print("hell" in str1) # expecting ...False
    
    print(len(str3))
    print(max(str3))
    print(min(str3)) # prints a space character
    
    stripped_str3 = str3.replace(' ', '')
    print(min(stripped_str3))
    
    print(str2.upper())
    print(str2)
    
    str2 = str2.upper()
    print(str2)
    
main()






