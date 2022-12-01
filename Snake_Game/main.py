import time
from turtle import Screen
from scoreboard import ScoreBoard

from food import Food
from snake import Snake

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor('black')
scr.title('My snake Game')
scr.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game = True
while game:
    scr.update()
    time.sleep(.1)
    snake.move()

    # collision w food. and update score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.current_score()

    # detect wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # detect tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

scr.exitonclick()
