from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.teleport(0, 270)
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
    def game_over(self):
        self.teleport(0,0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
    def t_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))
