from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

race_is_on = False
user_bet = screen.textinput("Place a Bet", "Which turtle will win the race??")
colors = ["red", "green", "blue", "yellow", "violet", "orange"]
x = -230
y = 100
all_turtles = []


for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x, y)
    turtle_index += 1
    y = y-30
    all_turtles.append(turtle)


if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            print(f"{turtle.pencolor()} has won")

            if turtle.pencolor() == user_bet:
                print(f"you have won the bet .The winner turtle is {turtle.pencolor()}")

            else:
                print(f"you have lost the bet .The winner turtle is {turtle.pencolor()}")
            race_is_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)






screen.exitonclick()