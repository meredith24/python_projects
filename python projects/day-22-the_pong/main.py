from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
import random
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) #animasyonlar kapatılıyor.

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update() #animasyonları kapattığımız için ekranı yenilememiz gerekiyor.
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320: # ikinci koşulu eklemezsek uzaklık koşulu sağlandığı için çubuk boyunca bounce aktif oluyor.
        ball.paddle_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() == 390:
        scoreboard.l_point()
        ball.reset_position()



    if ball.xcor() == -390:
        scoreboard.r_point()
        ball.reset_position()







screen.exitonclick()