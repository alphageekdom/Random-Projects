from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("TMNT  🐢  Race")
screen.setup(width=500, height=500)
screen.bgcolor("forestgreen")
run_race = False

def make_field():
    dirt = Turtle()
    dirt.speed(0)
    dirt.hideturtle()
    dirt.pendown()
    dirt.color("chocolate")
    dirt.begin_fill()
    dirt.penup()
    dirt.goto(x=-250, y=200)
    for _ in range(2):
        dirt.forward(500)
        dirt.right(90)
        dirt.forward(400)
        dirt.right(90)
    dirt.end_fill()


def finish_line():
    line = Turtle()
    line.speed(0)
    gap_size = 20
    line.shape("square")
    line.penup()
    # White Row 1
    line.color("white")
    for i in range(10):
        line.goto(210, (190 - (i * gap_size * 2)))
        line.stamp()
    # White Row 2
    for i in range(10):
        line.goto(210 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
        line.stamp()
    # Black Row 1
    line.color("black")
    for i in range(10):
        line.goto(210, (170 - (i * gap_size * 2)))
        line.stamp()
    # Black Row 2
    for i in range(10):
        line.goto(210 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
        line.stamp()


def turtle_runners():
    colors = ["red", "blue", "green", "gold", "purple", "pink"]
    turtle_coord = [-120, -70, -20, 30, 80, 130]
    all_turtles = []
    for turtle_runners in range(0, 1):
        new_turtle = Turtle(shape="turtle")
        new_turtle.pu()
        new_turtle.color(colors[turtle_runners])
        new_turtle.goto(x=-240, y=turtle_coord[turtle_runners])
        all_turtles.append(new_turtle)
    return all_turtles


def game():
    make_field()
    finish_line()
    runners = turtle_runners()
    user_bet = screen.textinput(
        title="Make bet", prompt="      Which turtle will win?")
    if user_bet:
        run_race = True
    while run_race:
        for turtle in runners:
            if turtle.xcor() > 190:
                winning_turtle = turtle.pencolor()
                run_race = False
                for i in range(72):
                    turtle.right(5)
                    turtle.shapesize(2.5)
                if winning_turtle == user_bet:
                    print(f"You won! The {winning_turtle} turtle won!")
                else:
                    print(f"You lost! The {winning_turtle} turtle won!")
            pace = random.randint(0, 10)
            turtle.forward(pace)


game()
while screen.textinput(title="", prompt="Do you want to bet again? (Y/N)").lower() == "y":
    game()
screen.exitonclick()
