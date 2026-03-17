import colorgram


# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r # geçişli kullanıldığı aklıma gelmedi.
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(tuple)
#
# print(rgb_colors)

import random
import turtle
from turtle import Turtle, Screen


color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 234), (222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]


tim = Turtle()
my_screen = Screen()
my_screen.colormode(255)
my_screen.setworldcoordinates(-100, -100, 600, 600)


def draw_hirst_painting(size):
    for n in range(1, size+1):
        for i in range(10):
            tim.pencolor(random.choice(color_list))
            tim.dot(20)
            tim.penup()
            tim.forward(50)


        tim.setx(0)
        tim.sety(50*n)

draw_hirst_painting(10)










my_screen.exitonclick()