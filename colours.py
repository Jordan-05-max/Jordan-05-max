"""from turtle import *
from colorsys import *

bgcolor("black")
width(2)
seth(45)
speed(0)
n = 180

for i in range(n):
    c = hsv_to_rgb(i / 6, i / n, 1)
    fillcolor(c)
    begin_fill()
    rt(90)
    circle(i * 1, 90)
    end_fill()
    rt(60)
ht()
done()
"""
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(180)
    if abs(pos())<1:
        break
end_fill()
done()