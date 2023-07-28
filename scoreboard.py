from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_LOCATION = (-280, 250)
SPEED_INCREMENT = 0.5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.game_speed = 0.1
        self.penup()
        self.hideturtle()

    def update_score(self):
        self.goto(SCORE_LOCATION)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def speed_up(self):
        self.game_speed *= SPEED_INCREMENT

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
