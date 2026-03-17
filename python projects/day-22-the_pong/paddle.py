from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def up(self):
        if self.ycor() > 200:
            pass
        else:
            self.sety(self.ycor() + 40)

    def down(self):
        if self.ycor() < -200:
            pass
        else:
            self.sety(self.ycor() - 40)