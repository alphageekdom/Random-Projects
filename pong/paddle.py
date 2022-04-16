from turtle import Turtle, Screen

class Paddle(Turtle):
    
    def __init__(self, position) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.speed(0)
        self.screen = Screen()
        self.screen.tracer(0)
    
    def up(self):
        """Moves paddle up"""
        self.speed(0)
        new_y = self.ycor() + 75
        self.goto(self.xcor(), new_y)
        self.screen.update()
    
    def down(self):
        """Moves paddle down"""
        self.speed(0)
        new_y = self.ycor() - 75
        self.goto(self.xcor(), new_y)
        self.screen.update()