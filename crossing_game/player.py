from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        """Makes turtle"""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        """Moves turtle up"""
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """Moves turtle down"""
        self.forward(MOVE_DISTANCE * -1)

    def go_to_start(self):
        """Respawn at start a every new level"""
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        """Check if the turtle is past the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
