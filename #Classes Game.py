# Classes Game
import turtle
import random
import math

# set ups screen 
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Turtle Game")
wn.bgpic("space_invaders_background.gif")
wn.register_shape("player.gif")
# Speed the game 
wn.tracer(0)

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0 

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="left", font=("Arial", 14, "normal"))
         
    def change_score(self, points):
        self.score += points  
        self.update_score()

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(10)

    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300,300)
        self.goto(300,-300)
        self.goto(-300,-300)



class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.speed =1

    def move(self):
        self.forward(self.speed)

        #Border Checking 
        if self.xcor()>290 or self.xcor() <-290:
            self.left(60)
        if self.ycor() >290 or self.ycor()< -290:
            self.left(60)

    def turnleft(self):
        self.left(30)
    def turnright(self):
        self.right(30)
    def turnback(self):
        self.back(30)
    def increasespeed(self):
        self.speed += 1
class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("player.gif")
        self.speed = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))
    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def move(self):
        self.forward(self.speed)

        # Border Checking 
        if self.xcor()>290 or self.xcor() <-290:
            self.left(60)
        if self.ycor() >290 or self.ycor()< -290:
            self.left(60)   

def isCollision(t1,t2):
    a=t1.xcor()-t2.xcor()
    b=t1.ycor()-t2.ycor()
    distance=math.sqrt((a ** 2) + (b ** 2 ))
    if distance <20:
        return True
    else:
        return False  
# Create multiple goals
goals=[]
for count in range(8):
    goals.append(Goal())  
# Create class instance

player= Player()
border = Border ()
goal = Goal()
game = Game()
# draw the border
border.draw_border()
# Keyboard 
turtle.listen()
turtle.onkey(player.turnright, "a")
turtle.onkey(player.turnleft,  "d")
turtle.onkey(player.increasespeed, "w")
turtle.onkey(player.turnback, "s")
# Main Loop
while True:
    player.move()
    goal.move()
    wn.update()
    for goal in goals:
        goal.move()
   
    #check collission
    if isCollision(player, goal):
        goal.jump()
        game.change_score(10)

