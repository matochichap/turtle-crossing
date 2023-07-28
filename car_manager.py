from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        rand_y = random.randint(-240, 240)
        self.setposition(320, rand_y)

    def move(self):
        self.fd(STARTING_MOVE_DISTANCE)
