from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title(" MY SNAKE GAME ")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True


def play_game():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            score.increase_score()
            snake.extend_snake()
        # collision with the wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            # game_is_on = False
            score.reset()
            snake.reset()

        for segment in snake.segment[1:]:
            if snake.head.distance(segment) < 15:
                # game_is_on = False
                score.reset()
                snake.reset()


play_game()

screen.exitonclick()
