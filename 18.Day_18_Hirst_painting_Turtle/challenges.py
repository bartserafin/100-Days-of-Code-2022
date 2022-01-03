# Importing Modules
# import turtle < -- use this if you use the module only a few times
# tim = turtle.Turtle()
# from turtle import Turtle < -- use this if you use the module often
# tim = Turtle()
# from turtle import * < -- DO NOT use this, it's confusing
# tim = Turtle()
# from turtle import Turtle as tim < -- use alias if you know your variable names might collide with package's names
# tim :D

from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("DarkCyan")

# Challenge 1 - draw a square

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)


# Challenge 2 - draw a dashed line

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Challenge 3 - draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon with edges of length 100
# each shape of random color

turtle.colormode(255)


def random_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    color = (r, g, b)
    return color


# def to ask for number of sides

# def draw_shape(num_sides):
#     tim.color(random_color())
#
#     for sides in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#
#
# for side in range(3, 11):
#     draw_shape(side)

# Challenge 4 - draw a random walk, make turtle go in random direction, with the same distance, with random color
# make thick lines, and make turtle faster

# turns = [0, 90, 180, 270]
#
# # thicker lines
# tim.pensize(10)
#
# # speed
# tim.speed('fastest')
#
# for move in range(300):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(turns))


# Challenge 5 - make a spirograph, a number of circles, radius 100, random color

tim.speed('fastest')


def draw_spirograph(steps):
    for angle in range(0, 360, steps):
        tim.color(random_color())
        tim.setheading(angle)
        tim.circle(100)

draw_spirograph(10)

screen.exitonclick()
