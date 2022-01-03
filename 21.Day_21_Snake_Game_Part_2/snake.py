from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    # Step 1: Create a snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    # Step 2: make snake move as linked squares
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
        self.head.forward(SPEED)

    # Step 3: make controls up, down, left, right
    def up(self):
        # Snake cant go up if facing down etc.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Step 4: Make snake extend after eating food
    def add_square(self, position):
        new_square = Turtle('square')
        new_square.penup()
        new_square.color('white')
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        self.add_square(self.squares[-1].position())

