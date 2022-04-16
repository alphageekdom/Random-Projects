from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays current level"""
        self.clear()
        self.current_level = f"Level: {self.level}"
        self.write(arg=self.current_level, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """Increases the level"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays 'GAME OVER' in the middle of the screen"""
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
