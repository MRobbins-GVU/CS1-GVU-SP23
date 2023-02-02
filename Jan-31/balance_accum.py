# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:41:12 2023

@author: mrobbins
"""


def balance_accum(princ, rate, years):
    """ Calculate compound interest """
    balance = princ
    
    for i in range(years):
        interest = balance * rate
        balance += interest
        
    return balance


def main():
    gains = balance_accum(1000, .05, 10)
    print(gains)
    
    principal = float(input("Starting principal:"))
    rate = float(input("Interest rate as decimal: "))
    time = int(input("Number of years in account: "))

    new_bal = balance_accum(principal, rate, time)
    print(new_bal)
    

main()