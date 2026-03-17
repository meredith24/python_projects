from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randrange(-250, 250))
        self.speed = speed

    def move(self):
        self.backward(self.speed)
        if self.xcor() == -250:
            self.clear()



    def increase_speed(self):
        self.speed += MOVE_INCREMENT




