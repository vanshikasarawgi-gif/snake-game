from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")  #background color of the screen
screen.title("My snake game")  #title of the screen
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
snake.move()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.count_score()
        snake.increase_length()

    #Detect collision with wall
    if (
    snake.head.xcor() > 290 or
    snake.head.xcor() < -290 or
    snake.head.ycor() > 290 or
    snake.head.ycor() < -290
    ):
        scoreboard.reset()
        snake.snake_reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.snake_reset()







screen.exitonclick()