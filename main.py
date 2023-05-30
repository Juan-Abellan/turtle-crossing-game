# IMPORTS
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# INITIAL SCREEN SETTINGS
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# CLASSES
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

# SCREEN LISTENING
screen.listen()  # Set focus on TurtleScreen (in order to collect key-events)
screen.onkey(player.go_up, key="Up")  # .onkey: Bind fun to key-release event of key.
# -----------------------------------------------------------------------------------------------------------------
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    # DETECTING COLLISION WITH CARS
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()


    # DETECTING SUCCESFUL CROSS
    if player.at_finish_line():
        player.goto_origin()
        car_manager.new_level()

        score_board.level_up()
        score_board.update_scoreboard()
# -----------------------------------------------------------------------------------------------------------------
# EXIT SCREEN SETTINGS
screen.exitonclick()
