import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play = Player()
car = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(play.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    # detect collision with car
    for cars in car.all_cars:
        if play.distance(cars) < 20:
            game_is_on = False
            score_board.game_over()

    # turtle at top
    if play.ycor() > 280:
        play.go_to_start()
        car.lvl_up()
        score_board.inc_lvl()


screen.exitonclick()
