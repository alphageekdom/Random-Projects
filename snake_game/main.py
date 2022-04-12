from turtle import Turtle, Screen
import time
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Solid 🐍 Game")


def create_snake():
    snake_position = [(0, 0), (-20, 0), (-40, 0)]
    for position in snake_position:
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.goto(position)


create_snake()
screen.exitonclick()