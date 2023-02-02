# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:05:03 2023

@author: mrobbins
"""


def years_to_goal(principal, rate, goal_amt):
    balance = principal
    years = 0
    
    while balance < goal_amt:
        interest = balance * rate
        balance += interest
        
        years += 1
        
    return years


def main():
    print(years_to_goal(1000, .0001, 1000000))
    print(years_to_goal(1000, .01, 1000000))
    print(years_to_goal(1000, .03, 1000000))
    print(years_to_goal(1000, .10, 1000000))
    print(years_to_goal(1000, 1.0, 1000000))
    
main()
