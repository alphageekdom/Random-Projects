from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
from turtle import Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("🐢 Crossing Game")
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    # Detect collision with carr
    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            game_on = False
            scoreboard.game_over()

    # Check if at finish line
    if player.at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
