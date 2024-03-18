from turtle import Screen, Turtle
from src.players import Player, Shooting
from src.scoreboard import Scoreboard
from src.asteroids import Asteroid
import random
import time

# Constants
BG_PICS = ['bg', 'background']
random_appear_threshold = 150

def check_collision(obj1, obj2):
    """Check for collision between two objects."""
    obj1_x, obj1_y = obj1.xcor(), obj1.ycor()
    obj2_x, obj2_y = obj2.xcor(), obj2.ycor()
    obj1_width, obj1_height = obj1.shapesize()[0] * 20, obj1.shapesize()[1] * 20
    obj2_width, obj2_height = obj2.shapesize()[0] * 20, obj2.shapesize()[1] * 20

    return (obj1_x - obj1_width/2 < obj2_x + obj2_width/2 and
            obj1_x + obj1_width/2 > obj2_x - obj2_width/2 and
            obj1_y - obj1_height/2 < obj2_y + obj2_height/2 and
            obj1_y + obj1_height/2 > obj2_y - obj2_height/2)

def create_asteroid():
    """Create a new asteroid."""
    asteroid = Asteroid()
    asteroids.append(asteroid)

try:
    # Initialize screen
    screen = Screen()
    screen.bgpic(f'imgs/{random.choice(BG_PICS)}.gif')
    screen.setup(width=1000, height=700)
    screen.cv._rootwindow.resizable(False, False)

    # Set up game
    difficulty = screen.textinput("Game Difficulty", "Choose difficulty level (easy, medium, hard, expert):").lower()
    difficulty_levels = {"easy": (0.03, 200), "medium": (0.03, 150), "hard": (0.03, 100), "expert": (0.03, 50)}
    delay, random_appear_threshold = difficulty_levels.get(difficulty, (0.02, 150))

    screen.tracer(0)

    # Create player and shooting mechanism
    player = Player(screen, x=-450)
    shooting = Shooting(player)
    scoreboard = Scoreboard()
    screen.listen()

    # Asteroids management
    asteroids = []

    is_game_over = False

    while not is_game_over:
        time.sleep(delay)
        shooting.move()
        shooting.fire()

        # Create new asteroid randomly
        if random.randint(0, random_appear_threshold) == 1:
            create_asteroid()

        # Move player
        player.move_to()

        # Move and check collisions for each asteroid
        for asteroid in asteroids:
            asteroid.move()

            # Remove asteroids that are out of bounds
            if asteroid.xcor() < -500:
                asteroid.clear()
                asteroid.hideturtle()
                asteroids.remove(asteroid)

                is_game_over = True

            # Check for collisions between shooting and asteroid
            if check_collision(shooting, asteroid):
                shooting.reset_state()
                asteroid.clear()
                asteroid.hideturtle()
                asteroids.remove(asteroid)
                delay -= 0.001
                random_appear_threshold -= 1

                if delay < 0:
                    delay = .003
                if random_appear_threshold < 10:
                    random_appear_threshold = difficulty_levels.get(difficulty, (0.02, 150))

                scoreboard.add_asteroid()

        screen.update()

    if is_game_over:
        scoreboard.game_over()
    # Start the game loop
    screen.mainloop()

except KeyboardInterrupt:
    print("Game exited by user.")
except Exception as e:
    print("An error occurred while running the game:", str(e))
