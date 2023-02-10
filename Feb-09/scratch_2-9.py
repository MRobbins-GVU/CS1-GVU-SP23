# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:24:34 2023

@author: Robbins
"""

def main():
    items = [1, 56, 3, 9, 7]
    
    print(items[4])
    
    print(items[1:4])
    
    print(items[0:4:2])
    
    # Prints everything up to but not including index 2
    print(items[:2])
    
    # Prints everything from index 2 to the end
    print(items[2:])
    
    # Prints every other item from the start to the end.
    print(items[::2])
    
    # Prints every other item from the end to the start
    print(items[::-2])
    
    # Prints the middle of the list backwards
    print(items[-2:-5:-1])
    
    print("~~~~~~~~~~~~~~~")
    
    list_1 = [0, 2, 3, 4]
    list_2 = [1, 5, 7, 3]
    
    new_list = list_1 + list_2
    print(new_list)
    
    print(list_1)
    list_1 += list_2
    print(list_1)
    
main()






