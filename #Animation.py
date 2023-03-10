# Animation
import turtle
import time

wn = turtle.Screen()
wn.title("Animation")
wn.bgcolor("black")
# Register shapes
wn.register_shape("invader.gif")
wn.register_shape("invader.gif")

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("invader.gif")
        self.color("green")
        self.frame = 0
        self.setposition(-300,300)
        self.frames = ["invader.gift","circle"]

    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape (self.frames[self.frame])

        # set Timer
        wn.ontimer(self.animate, 500)

player = Player()
player.animate()

player2 = Player()
player2.goto(0, 100)
player2.animate()

player3 = Player()
player3.goto(0, -100)
player3.animate()

while True:
	wn.update()
	print("Main Loop")

wn.mainloop()
    
