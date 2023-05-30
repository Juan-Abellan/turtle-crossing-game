# IMPORTS
from turtle import Turtle
from random import randint, choice

# CONSTANTS
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    Contains everything related to the cars flow across the screen.
    """
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        """
        Creates a new car.
        """
        y_random = randint(-250, 250)
        random_tempo = randint(1,6) # To reduce the tempo the cars are created.
        if random_tempo == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(300, y_random)
            self.all_cars.append(new_car)

    # MOVE FUNCTIONS
    def car_move(self):
        """
        Makes the car move.
        """
        for car in self.all_cars:
            car.backward(self.speed)

    def new_level(self):
        """
        Each time the turtle crosses the road increases the speed of the cars.
        """
        self.speed += MOVE_INCREMENT

