
# TODO: 1. Make a paddle class that that can be moved vertically across the screen

# TODO: 2. Make ball that goes in a specific direction until it hits a wall or a paddle

# TODO: 3. Create a scoreboard display that tracks when the ball pass the left or right side of the screen

# TODO: 4. Create a dotted line down the middle splitting the screen in to two sides

# My classes: Paddle() , Ball() , Scoreboard()

from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")
screen.title("PONG Game")
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle()

screen.listen()
screen.onkey(fun = go_up, key = "Up")
screen.onkey(fun = go_down, key = "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()