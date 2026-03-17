from turtle import Turtle
from snake import Snake
FONT = ('Arial', 24, 'normal')
ALIGNMENT = "center"



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.initial_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score}', align=ALIGNMENT, font=FONT )
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def initial_high_score(self):
        with open("data.txt", mode="r") as file:
            initial_high_score = file.read()
            return int(initial_high_score)




    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()




    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

