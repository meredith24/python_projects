import time
from turtle import Screen

from plotly.data import carshare

from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player_1 = Player()
screen.listen()
screen.onkey(player_1.move, "Up")

scoreboard = Scoreboard()
cars = []
car_speed = STARTING_MOVE_DISTANCE

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter % 6 == 0:
        car = CarManager(car_speed)
        cars.append(car)

    for car in cars:
        car.move()
        if car.distance(player_1) < 20:
            scoreboard.game_over()
            game_is_on = False


    if player_1.ycor() == 300:
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        player_1.goto_start()
        for car in cars:
            car.increase_speed()
        car_speed += MOVE_INCREMENT
        print(car_speed)






screen.exitonclick()
