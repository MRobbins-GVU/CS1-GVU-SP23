# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 19:25:41 2023

@author: Robbins
"""

from turtle import *

def move(distance):
    """Move forward, reverse at the right side."""
    forward(distance)
    if xcor() > 320: 
        setheading(180) # either turn 180 degrees, or set heading to due left

def main():
    shape("circle")
    speed(0)
    penup()
    for x in range(100):
        move(10)
    
    exitonclick()
    
main()