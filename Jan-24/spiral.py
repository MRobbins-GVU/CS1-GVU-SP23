# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:00:58 2023

@author: mrobbins
"""

from turtle import *

def spiral(first_step, angle, gap):
    """ first_step is how far the turtle moves before turning
        angle is the angle the turtle turns
        gap is how much the turtle reduces its step
    """
    while first_step > 0:
        forward(first_step)
        left(angle)
        first_step -= gap

def main():
    spiral(100, 71, 2)
    spiral(100, 91, -5) 
    exitonclick()
    
main()