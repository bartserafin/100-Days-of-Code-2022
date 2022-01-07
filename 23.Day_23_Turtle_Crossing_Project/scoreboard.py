from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level_number = 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f'Level:{self.level_number}', align='left', font=FONT)

    def update_score(self):
        self.level_number += 1
        self.display_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write('GAME OVER.', align='center', font=FONT)
