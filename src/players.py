from turtle import Turtle

class Player(Turtle):
    """A class representing the player in the game."""
    
    def __init__(self, screen, x: int = 0, y: int = 0):
        """Initialize the player object."""
        super().__init__(shape='triangle')

        self.penup()
        
        self.shapesize(stretch_wid=3, stretch_len=4)
        self.color('blue')
        self.goto((x,y))
        self.screen = screen
    
    def move_to(self):
        """Set up key listeners for moving the player."""
        self.screen.onkey(self.move_up, 'w')
        self.screen.onkey(self.move_down, 's')
        self.screen.onkey(self.move_up, 'Up')
        self.screen.onkey(self.move_down, 'Down')
    
    def move_up(self):
        """Move the player upwards."""
        self.goto((self.position()[0], self.position()[1]+50))

    def move_down(self):
        """Move the player downwards."""
        self.goto((self.position()[0], self.position()[1]-50))

class Shooting(Turtle):
    """A class representing the shooting mechanism in the game."""
    
    def __init__(self, player):
        """Initialize the shooting mechanism."""
        super().__init__()
        self.player = player
        self.color("yellow")
        self.shape("triangle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.state = "ready"

    def move(self):
        """Move the projectile."""
        if self.state == "fire":
            self.setx(self.xcor() + 15)
        if self.xcor() > 500:
            self.reset_state()

    def fire(self):
        """Fire the projectile."""
        if self.state == "ready":
            self.goto(self.player.xcor(), self.player.ycor())
            self.state = "fire"

    def reset_state(self):
        """Reset the state of the projectile."""
        self.goto(self.player.xcor(), self.player.ycor())
        self.state = "fire"
