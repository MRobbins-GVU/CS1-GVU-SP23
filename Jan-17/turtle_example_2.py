# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:17:57 2023

@author: mrobbins
"""

from turtle import *

speed(1)

penup()
goto(0, -100)
goto(-200, -100)
pendown()

fillcolor("green")
begin_fill()
goto(-200, 100)
goto(200, -100)
goto(200, 100)
goto(-200, -100)
end_fill()


exitonclick()