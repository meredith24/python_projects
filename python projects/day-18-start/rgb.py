import random
import turtle  # class'ı import etsek bile kütüphane import olmuyor yani.
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.speed("fastest")

def draw_spirograph(size_of_gap, radius):
    for i in range(0, 361, size_of_gap):
        tim.color(random_color())
        tim.setheading(i)
        tim.circle(radius)

draw_spirograph(3, 100)






screen.exitonclick()