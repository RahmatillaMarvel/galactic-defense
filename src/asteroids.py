import turtle
import random

class Asteroid(turtle.Turtle):
    """A class representing an asteroid in the game."""
    
    def __init__(self):
        """Initialize the asteroid object."""
        super().__init__()
        self.shape("square")
        self.color("grey")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=4)
        self.goto(500, random.randint(-250, 250))
        self.dx = random.randint(1, 4)

    def move(self):
        """Move the asteroid to the left."""
        self.setx(self.xcor() - self.dx)
