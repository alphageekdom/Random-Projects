from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.speed(0)
    
    def up(self):
        new_y = self.ycor() + 75
        self.goto(self.xcor(), new_y)
        self.speed(0.09)
    
    def down(self):
        new_y = self.ycor() - 75
        self.goto(self.xcor(), new_y)
        self.speed(0.09)