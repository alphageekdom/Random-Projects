from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "a") as data:
                data.write(f"\n{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increases the score"""
        self.score += 1
        self.update_scoreboard()
    
    #def game_over(self):
    #    """Displays 'GAME OVER' in the middle of the screen"""
    #    self.goto(x=0, y=0)
    #    self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
