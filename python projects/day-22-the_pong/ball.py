from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.xincor = 0
        self.yincor = 0
        self.goto(self.xincor ,self.yincor)
        self.x_move = random.randint(1, 6)
        self.y_move = random.randint(1, 6)
        self.move_speed = 0.1


    def move(self):

        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self):
        self.y_move = -self.y_move

    def paddle_bounce(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset_position(self):

        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_bounce()














