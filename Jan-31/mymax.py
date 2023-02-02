# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:51:21 2023

@author: mrobbins
"""

def mymax(x, y):
    """ Compare 2 values and return whichever 
    is greater """
    if x > y:
        return x
    else:
        return y


def main():
    print(max(1, 2)) # Built in Python function
    
    larger = mymax(5, 7)
    print(larger)
    
    larger2 = mymax(3,3)
    print(larger2)
    
    larger3 = mymax(30, 17)
    print(larger3)
    
main()