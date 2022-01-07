import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPEED = 0.1  # Speed of the game, difficulty

# Create screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# Create turtle and move it
player = Player()
player.create_player()

# Create scoreboard
scoreboard = Scoreboard()

# Create cars
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move_up, key='w')
screen.onkey(fun=player.move_down, key='s')
screen.onkey(fun=player.move_left, key='a')
screen.onkey(fun=player.move_right, key='d')

# --- GAME LOOP --- #
game_is_on = True

while game_is_on:

    time.sleep(SPEED)
    screen.update()

    # Spawn cars
    car_manager.create_car()
    car_manager.move_cars()

    # check if reached top wall
    if player.ycor() > SCREEN_HEIGHT / 2 - 20:
        scoreboard.update_score()
        player.create_player()
        car_manager.next_level()

    # check collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

# EXIT
screen.exitonclick()
