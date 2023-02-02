# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:21:06 2023

@author: mrobbins
"""


def balance(princ, rate, time):
    """ Calculate compound interest """
    return princ*(1 + rate)**time


def main():
    gains = balance(1000, .05, 10)
    print(gains)
    
    principal = float(input("Starting principal:"))
    rate = float(input("Interest rate as decimal: "))
    time = int(input("Number of years in account: "))

    new_bal = balance(principal, rate, time)
    print(new_bal)
    

main()




