# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:42:27 2023

@author: Robbins
"""

def mysum(items):
    """ Return the sum of the values in items """
    total = 0
    
    for item in items:
        print(item)
        total += item
    
    return total
    
def main():
    data_list = [1, 9, 7, 3, 4, 5, 6, -5]
    
    print("Total:", mysum(data_list))
    
    print("Python sum:", sum(data_list))
    
    sorted_list = sorted(data_list)
    
    print(sorted_list)
    
main()