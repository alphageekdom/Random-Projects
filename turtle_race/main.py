from scoreboard import Scoreboard
from runners import Runners
from turtle import Screen
from field import Field
import random
import time


# Create Screen
screen = Screen()
screen.title("TMNT  🐢  Race")
screen.setup(width=500, height=500)
screen.bgcolor("forestgreen")
screen.tracer(0)

# Create the turtles that are running
runners = Runners()
scoreboard = Scoreboard()
field = Field()


# Main game loop
run_race = False
field.make_field()
field.checkered_line()
runners.make_runners()
screen.update()
user_bet = screen.textinput(
    title="Make bet", prompt="      Which turtle will win?")
if user_bet:
    run_race = True
while run_race:
    screen.update()
    time.sleep(0.1)
    for turtle in runners.all_turtles:
        if turtle.xcor() > 189:
            for _ in range(72):
                screen.update()
                turtle.right(5)
                turtle.shapesize(2.5)
            run_race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle won!")
                scoreboard.increase_score()
            else:
                print(f"You lost! The {winning_turtle} turtle won!")
        pace = random.randint(0, 10)
        turtle.forward(pace)


screen.exitonclick()
