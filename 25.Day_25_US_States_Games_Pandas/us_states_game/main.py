# Make a game where you have to name all Us States, after the name is inputted it should appear on a map
# like here:
# https://www.sporcle.com/games/g/states

import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')

# Create turtle for background image
background = 'blank_states_img.gif'
screen.addshape(background)
turtle.shape(background)

# Create turtle for writing state names
state_name = turtle.Turtle()
state_name.hideturtle()
state_name.penup()

# This was used to generate the 50_states.csv file
# Get the mouse click coordinates
# def get_mouse_click_x_y(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick

# create DataFrame from 50_states.csv
data = pandas.read_csv('50_states.csv')
data_states = data.state.to_list()

# a list for keeping the correct answers
guessed_list = []


# --- GAME LOOP --- #
while len(guessed_list) < 50:
    # Ask user for a guess and display score
    state_guess = screen.textinput(title=f"{len(guessed_list)}/{len(data_states)} Correct States",
                                   prompt="What is another state's name?")
    state_guess = state_guess.title()

    # check for exit
    if state_guess == 'Exit':

        # create a csv with all missed states
        missing_states = []
        for state in data_states:
            if state not in guessed_list:
                missing_states.append(state)
        states_to_remember = pandas.DataFrame(missing_states)
        states_to_remember.to_csv('states_to_learn.csv')
        break

    # check if guess correct
    for state in data.state:
        if state_guess == state:

            #  get a data in a row for the guessed state
            state_cor = data[data.state == state_guess]

            #  access the state's coordinates
            x_cor = int(state_cor.x)
            y_cor = int(state_cor.y)
            state_name.goto(x_cor, y_cor)

            #  write the correct guess on the map
            state_name.write(f"{state_guess}", align='center', font=('Courier', 10, 'normal'))

            #  update the scoreboard
            guessed_list.append(state_guess)

