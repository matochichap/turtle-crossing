import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
all_cars = []
count = 0

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.game_speed)
    screen.update()
    scoreboard.update_score()

    # generate moving cars (not sure how to put this in CarManager class)
    if count == 5:
        new_car = CarManager()
        all_cars.append(new_car)
        count = 0
    for car in all_cars:
        car.move()
    count += 1

    # detect collision between car and player
    for car in all_cars:
        if player.distance(car) < 27:
            scoreboard.game_over()
            game_is_on = False

    # proceed to next level
    if player.at_finish_line():
        scoreboard.score += 1
        scoreboard.speed_up()
        scoreboard.clear()

screen.exitonclick()
