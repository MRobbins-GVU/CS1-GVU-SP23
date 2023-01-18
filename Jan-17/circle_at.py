# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:00:02 2023

@author: mrobbins
"""

from turtle import *

def circle_at(x_coordinate, y_coordinate):
    penup()
    goto(x_coordinate, y_coordinate)
    pendown()
    circle(50)
    

def main():
    pensize(7)
    circle_at(200, -100)
    circle_at(200, 100)
    
    fillcolor("green")
    begin_fill()
    circle_at(0,0)
    end_fill()
    
    exitonclick()
    
    
main()
