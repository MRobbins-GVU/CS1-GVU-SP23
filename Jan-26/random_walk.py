# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:41:44 2023

@author: mrobbins
"""

from turtle import *
from random import randrange

def random_step(distance):
    turn_degrees = randrange(0, 360, 90)
    left(turn_degrees)
    forward(distance)

def main():
    speed(0)
    #for x in range(100):
    #    random_step(25)
    
    length = int(input("How long to stride? : "))
    
    while abs(xcor()) < 300 and abs(ycor()) < 300:
        random_step(length)
    
    exitonclick()
    
    
main()






