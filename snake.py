from turtle import Turtle,Screen
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
class Snake:
    screen=Screen()
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head=self.turtles[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_seg(i)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
    def add_seg(self,pos):
        tim = Turtle(shape="square")
        tim.color("White")
        tim.penup()
        tim.goto(pos)
        self.turtles.append(tim)
    def extend(self):
        self.add_seg(self.turtles[-1].position())
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)