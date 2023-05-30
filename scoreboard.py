# IMPORTS
from turtle import Turtle

# CONSTANTS
FONT = ("Consolas", 24, "normal")


class Scoreboard(Turtle):
    """
    Contains everything related to the score board.
    """

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the score board clearing the previous one.
        """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """
        Increases the the level after a succesful cross.
        """
        self.level += 1

    def game_over(self):
        """
        Writes Game Over after having a collision with a car.
        """
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
