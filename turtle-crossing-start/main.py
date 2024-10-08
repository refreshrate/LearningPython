import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# from scoreboard import Scoreboard
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

player = Player()

car_manager = CarManager()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    Scoreboard()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    #detect crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()
screen.exitonclick()
