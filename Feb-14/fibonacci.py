# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:33:54 2023

@author: mrobbins
"""

def fibo(n):
    """Return the first n values of the Fibonacci sequence"""
    fibo_list = [1, 1]
    while len(fibo_list) < n: 
        # calculate next value
        next_value = fibo_list[-1] + fibo_list[-2] 
        # add next value to fibo_list
        fibo_list += [next_value]
    
    return fibo_list
    

def main():
    print(fibo(5)) # 1, 1, 2, 3, 5
    print(fibo(10)) # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    
main()