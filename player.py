# IMPORTS
from turtle import Turtle

# CONSTANTS
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    '''
    Contains everything related to the player.
    '''
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # MOVE FUNCTIONS
    def go_up(self):
        """
        Makes the turtle go north direction.
        """
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        """
        Returns True or False depending to the location of the turtle.
        """
        return True if self.ycor() > FINISH_LINE_Y else False

    def goto_origin(self):
        """
        Sends the turtle to the starting point.
        """
        self.goto(STARTING_POSITION)
