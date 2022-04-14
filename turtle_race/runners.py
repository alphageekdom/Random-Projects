from turtle import Turtle

COLORS = ["red", "blue", "green", "gold", "purple", "pink"]
TURTLE_COORD = [-120, -70, -20, 30, 80, 130]

class Runners():
    
    def __init__(self):
        self.all_turtles = []
        self.speed = 20
    
    def make_runners(self):
        for turtle_runners in range(0, 6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.pu()
            new_turtle.color(COLORS[turtle_runners])
            new_turtle.goto(x=-240, y=TURTLE_COORD[turtle_runners])
            self.all_turtles.append(new_turtle)