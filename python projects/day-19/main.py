import turtle
from turtle import Turtle, Screen # Turtle ve Screen class. Baş harfleri büyük olur genelde.
import random

is_race_on = False
screen = Screen() # nesne oluşturduk.

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]

all_turtles = []
for color in colors: # burada nesne oluştururken, loopta, aynı ismi taşısa bile farklı nesneler oluşuyor. ama ben burada farklı isimde oluşturmayı tercih ettim.

    color_turtle = Turtle(shape="turtle") #nesnenin özellikleri, nesneyi oluştururken belirleyebiliyoruz.
    color_turtle.color(color)
    color_turtle.penup()
    initial_position = colors.index(color)*30-60
    color_turtle.goto(x=-230, y=initial_position)
    all_turtles.append(color_turtle)

if user_bet: # user_bet değeri girilince döngüyü aktif edecek.
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)

        if turtle.xcor() >= 250:
            is_race_on = False

            if turtle.pencolor() == user_bet:
                print("You Win!")
            else:
                print(f" {turtle.pencolor()} turtle wins Your bet Lose!")













screen.exitonclick()