from turtle import Turtle

GAP_SIZE = 20

class Field():
    
    def __init__(self):
        self.dirt = Turtle()
        self.line = Turtle()
    
    def make_field(self):
        self.dirt.speed(0)
        self.dirt.hideturtle()
        self.dirt.pendown()
        self.dirt.color("chocolate")
        self.dirt.begin_fill()
        self.dirt.penup()
        self.dirt.goto(x=-250, y=200)
        for _ in range(2):
            self.dirt.forward(500)
            self.dirt.right(90)
            self.dirt.forward(400)
            self.dirt.right(90)
        self.dirt.end_fill()
    
    
    def checkered_line(self):
        self.line.speed(0)
        self.line.shape("square")
        self.line.penup()
        # White Row 1
        self.line.color("white")
        for i in range(10):
            self.line.goto(210, (190 - (i * GAP_SIZE * 2)))
            self.line.stamp()
        # White Row 2
        for i in range(10):
            self.line.goto(210 + GAP_SIZE, ((190 - GAP_SIZE - (i * GAP_SIZE * 2))))
            self.line.stamp()
        # Black Row 1
        self.line.color("black")
        for i in range(10):
            self.line.goto(210, (170 - (i * GAP_SIZE * 2)))
            self.line.stamp()
        # Black Row 2
        for i in range(10):
            self.line.goto(210 + GAP_SIZE, ((210 - GAP_SIZE) - (i * GAP_SIZE * 2)))
            self.line.stamp()