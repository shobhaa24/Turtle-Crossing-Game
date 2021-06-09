from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.color("black")
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game over.", align="center", font=FONT)

    def update_score(self):
        self.penup()
        self.goto(-200,250)
        self.clear()
        self.write(f"Level {self.score}.", align="left", font=FONT)

    def level_up(self):
        self.score += 1
        self.update_score()
