# Motion
import turtle
import time
import math
# set up screen
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Motion")

GRAVITY = 0.1

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.speed = 20
               

    def move(self):
        self.goto(self.xcor(), self.ycor())

    def move(self):
        self.goto(self.xcor(), self.ycor())

    def move_left(self):
        self.setx(self.xcor() - self.speed)
    def move_right(self):
        self.setx(self.xcor() + self.speed)
    def move_up(self):
        self.sety(self.ycor() + self.speed)
    def move_down(self):
        self.sety(self.ycor() - self.speed)


player = Player()

wn.listen()
wn.onkey(player.move_left, "Left")
wn.onkey(player.move_right, "Right")
wn.onkey(player.move_up, "Up")
wn.onkey(player.move_down, "Down")


 # Main game loop
while True:
    player.move()