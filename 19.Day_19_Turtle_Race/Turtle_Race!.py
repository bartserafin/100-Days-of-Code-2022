import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

# Ask user for a BET
user_bet = screen.textinput(title='Make your bet', prompt="Enter a color: (red, orange, yellow, pink, blue, violet) ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

# Create race turtles
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_idx in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_idx])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_idx])
    all_turtles.append(new_turtle)

# Race loop
if user_bet:
    is_race_on = True

while is_race_on:

    # Turtle graphic is 40x40, 250 - 40/2 is when the turtle touches the edge
    # Check for winner
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is first!")
            else:
                print(f'You loose! The {winning_color} turtle is first!')
            is_race_on = False

    # if race is not over, move all turtles by random distance
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
