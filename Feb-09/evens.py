# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:52:32 2023

@author: Robbins
"""

def evens(items): 
    """ Return a list of all even values in items """
    
    results = []
    
    for item in items:
        if item % 2 == 0:
            results += [item]
            # results += list(item)

    #return results
    print(results)

def main():
    data = [93, 32, 28, 2, 56, 99, 17, 14, 3]
    even_data = evens(data)
    
    print(even_data)
    
    even_data += [4, 98, 36]
    
    print(even_data)


main()