# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:02:19 2023

@author: mrobbins
"""

def letter_grade(num_grade):
    # print(num_grade)
    if num_grade >= 90:
        if num_grade > 96: 
            print("A+")
        elif num_grade > 93:
            print("A")
        else:
            print("A-")
        print("A is for Awesome")

    elif num_grade >= 80:
        print("B is for B*tchin'")
        
    elif num_grade >= 70:
        print("C is for Cool Kids")

    elif num_grade >= 60:
        print("Doing great!")
        
    else:
        print("Fantastic!")


def main():
    letter_grade(95)
    letter_grade(88)
    letter_grade(72)
    letter_grade(69)
    letter_grade(57)
    # letter_grade("asdf") This throws an error
    
main()