# Turtle Graphichs game
import turtle
import math
import random

# Screen Setup
sc = turtle.Screen()
sc.bgcolor("lightgreen")
sc.tracer(3)

# Draw Border
Border = turtle.Turtle()
Border.up()
Border.setpos(-300, -300)
Border.down()
Border.pensize(3)
for side in range(4):
    Border.fd(600)
    Border.lt(90)
    Border.hideturtle()

# Player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("classic")
player.up()
player.speed(100)


# Create gols
maxGoals = 6
goals = []
for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].up()
    goals[count].speed(0)
    goals[count].setpos(random.randint(-300, 300), random.randint(-300, 300))

# Whole point of the game
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.up()
goal.speed(0)
goal.setpos(random.randint(-300, 300), random.randint(-300, 300))

# Set speed
speed = 1

# Functions
def Left():
    player.lt(45)

def Right():
    player.rt(45)

def SanicSpeed():
    global speed
    speed += 1
    if speed > 3:
        speed = 3

def SnailSpeed():
    global speed
    speed -=  1
    if speed < 1:
        speed = 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False


# Set key bindings
sc.listen()
sc.onkey(Left, "Left")
sc.onkey(Right, "Right")
sc.onkey(SanicSpeed, "Up")
sc.onkey(SnailSpeed, "Down")
while True:
    player.fd(speed)


 # Boundary Checking 
    if player.xcor() > 300 or player.xcor() < -300:
        player.rt(100)
    if player.ycor() > 300 or player.ycor() < -300:
        player.rt(100)

 # Collision checking
 
 

 # Move teh goal
    for count in range(maxGoals):
        goals[count].fd(1)
        goal.fd(1)
  # Boundary Checking  for goal turtle
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].rt(100)
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].rt(100)
        if goal.xcor() > 290 or goal.xcor() < -290:
            goal.rt(100)
        if goal.ycor() > 290 or goal.ycor() < -290:
            goal.rt(100)
        if isCollision(player, goals[count]):
            goals[count].setpos(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].rt(random.randint(0,300))


        if isCollision(player, goal):
            goal.setpos(random.randint(-300, 300), random.randint(-300, 300))
            goal.rt(random.randint(0,300))
            
            