    # DAY 19

# Event listeners
from turtle import Turtle, Screen, listen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear_screen():
    screen.clearscreen()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
