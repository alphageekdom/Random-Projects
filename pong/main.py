from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen
from ball import Ball
import time


screen = Screen()

screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PONG 🕹")
screen.tracer(0)


scoreboard = Scoreboard()
ball = Ball()


r_paddle = Paddle((450, 0))
l_paddle = Paddle((-460, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.momentum)
    screen.update()
    ball.move()

    # Ball hits upper or lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check if ball hit the left or right paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 340 or ball.distance(l_paddle) < 30 and ball.xcor() < -340:
        ball.bounce_x()

    # Left paddle scores
    if ball.xcor() > 500:
        ball.reset()
        scoreboard.l_point()

    # Right paddle scores
    if ball.xcor() < -500:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
