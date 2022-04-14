from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-200, y=200)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays scoreboard"""
        self.score_num = f"Score: {self.score}"
        self.write(arg=self.score_num, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score"""
        self.clear()
        self.score += 1
        self.update_scoreboard()