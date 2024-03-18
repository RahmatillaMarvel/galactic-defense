from turtle import Turtle

class Scoreboard(Turtle):
    """A class to represent the scoreboard in the game."""

    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.total_asteroids = 0
        self.goto(-200, 250)
        self.write(f"Asteroids destroyed: {self.total_asteroids}", align="center", font=("Arial", 30, "bold"))

    def add_asteroid(self):
        """Increment the number of destroyed asteroids and update the scoreboard."""
        self.total_asteroids += 1
        self.clear()
        self.write(f"Asteroids destroyed: {self.total_asteroids}", align="center", font=("Arial", 30, "bold"))
    
    def game_over(self):
        """Display the 'GAME OVER' message in the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
