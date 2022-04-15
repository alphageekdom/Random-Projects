from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.momentum = 0.1
    
    
    def move(self):
        """Moves the ball"""
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        """Check if ball hit upper/lower wall"""
        self.ymove *= -1
    
    def bounce_x(self):
        """Check if ball hit paddle"""
        self.xmove *= -1
        self.momentum *= 0.1
    
    def reset(self):
        """Resets ball in the middle"""
        self.goto(0, 0)
        self.momentum = 0.1
        self.bounce_x()