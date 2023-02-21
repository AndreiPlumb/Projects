import turtle
import random

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling ")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

#Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

#Create a list of good guys
goods = []

#Add the goods
for _ in range(20):
    good = turtle.Turtle()
    good.speed(0)
    good.shape("circle")
    good.color("blue")
    good.penup()
    good.goto(-100, 250)
    good.speed = random.randint(1, 3)
    goods.append(good)

#Create a list of bad guys
bads = []

#Add the goods
for _ in range(20):
    bad = turtle.Turtle()
    bad.speed(0)
    bad.shape("circle")
    bad.color("red")
    bad.penup()
    bad.goto(100, 250)
    bad.speed = random.randint(1, 3)
    bads.append(bad)    
#Add Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 250)
font =("Aria", 24, "normal")
pen.write("Score:{} Lives: {}".format(score, lives),align="center",font=font)

#Function
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"
    

#keyboard binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Main game loop
while True:
    #Update screen
    wn.update()
    
    #Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    #Move the goods
    for good in goods:
        y = good.ycor()
        y -= good.speed
        good.sety(y)

        #Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good.goto(x, y)

        #Check for collision
        if good.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score:{} Lives: {}".format(score, lives),align="center",font=font)

    
    #Move the bads
    for bad in bads:
        y = bad.ycor()
        y -= bad.speed
        bad.sety(y)

        #Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)

        #Check for collision
        if bad.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score:{} Lives: {}".format(score, lives),align="center",font=font)
        
wn.mainloop()