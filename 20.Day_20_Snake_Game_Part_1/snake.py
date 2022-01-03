from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()

    # Step 1: Create a snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle('square')
            new_square.penup()
            new_square.color('white')
            new_square.goto(position)
            self.squares.append(new_square)

    # Step 2: make snake move
    # take a snake to be 3 squares, we move the last square [index 2] to the position of the second square [index 1],
    # and the second square [1] to the location of the first square [0]
    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            # Grab coordinates from previous square
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            # Put coordinates into the next square
            self.squares[square_num].goto(new_x, new_y)

        # lastly, move the head of the snake
        self.squares[0].forward(SPEED)

    # Step 3: make controls for left and right
    def up(self):
        self.squares[0].setheading(90)

    def down(self):
        self.squares[0].setheading(270)

    def right(self):
        self.squares[0].setheading(0)

    def left(self):
        self.squares[0].setheading(180)

