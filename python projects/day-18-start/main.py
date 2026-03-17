from turtle import Turtle, Screen
import turtle # class'ı import etsek bile kütüphane import olmuyor yani.
import random
import math

tim = Turtle()
screen = Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_direction():
    direction = random.choice(["right", "left"])
    return direction

def distance(x1, y1):
    return math.sqrt(x1**2 + y1**2)

end_point_data = []
end_point_data_distance = []
screen.setworldcoordinates(-1000, -1000, 1000, 1000)


for i in range(10):
    tim.home()
    for n in range(0,50):
        tim.color(random_color())
        direction = random_direction()
        if direction == "right":
            tim.right(90)
        elif direction == "left":
            tim.left(90)
        tim.pensize(15)
        tim.speed(50)
        tim.forward(100)


    tim_position = tim.position()
    end_point_data.append(tim_position)



for i in end_point_data:
    d = distance(i[0], i[1])
    end_point_data_distance.append(d)



print(end_point_data)
print("\n")
print(end_point_data_distance)


screen.exitonclick()