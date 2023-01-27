# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:47:53 2023

@author: Robbins
"""

from turtle import *

def polygon(num_sides, length):
    """Draws a polygon with num_sides and length."""
    for x in range(num_sides):
        forward(length)
        left(360/num_sides)


def main():
    speed(1)

    for sides in range(3, 10):
        polygon(sides, 80)

    # polygon(3, 100)

    exitonclick()
    
main()