# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:08:12 2023

@author: mrobbins
"""

def find(target, items): 
    """Return the first position where target is
    located inside of items. Or, return -1 if target
    is not found inside items. """
    for i in range(len(items)):
        if target == items[i]:
            return i
    return -1
    
    
def main():
    list_1 = [3, 17, -32, 9]
    target_1 = 17
    find_1 = find(target_1, list_1)
    print(find_1)
    
    target_2 = 999
    find_2 = find(target_2, list_1)
    print(find_2)
    
    target_3 = 9
    find_3 = find(target_3, list_1)
    print(find_3)
    
    
    
main()







