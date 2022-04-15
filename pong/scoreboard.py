from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays scoreboard"""
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def r_point(self):
        """Increses score for right player"""
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        """Increases the score for left player"""
        self.l_score += 1
        self.update_scoreboard()
