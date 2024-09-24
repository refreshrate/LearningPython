from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-280, 280)
        self.hideturtle()
        self.write(f"Score= {self.score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score= {self.score + 1}")
