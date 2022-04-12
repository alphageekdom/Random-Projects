from turtle import Turtle
import time

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.make_snake()

    def make_snake(self):
        for position in START_POS:
            new_snake = Turtle(shape="square")
            new_snake.penup()
            new_snake.color("white")
            new_snake.goto(position)
            self.segments.append(new_snake)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIS)
