from turtle import Turtle,Screen
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

s=Snake()
f=Food()
score=Scoreboard()

screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.left,"Left")
screen.onkey(s.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    s.move()
    if s.head.distance(f)<15:
        f.refresh()
        s.extend()
        score.t_score()
    if s.head.xcor()>280 or s.head.xcor()<-280 or s.head.ycor()>280 or s.head.ycor()<-280:
        game_on = False
        score.game_over()
    for i in s.turtles[1:]:
        if s.head.distance(i)<10:
            game_on = False
            score.game_over()

screen.exitonclick()