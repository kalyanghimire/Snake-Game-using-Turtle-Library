
import random
import time
from snake import snake
from food import food
from turtle import Screen, Turtle
from scoreboard import Scoreboard
screen = Screen()
screen.listen()
food = food()
snake = snake()
snake.tracer()
game_is_on = 1
scoreboard = Scoreboard()
loop = True
while game_is_on == 1:
    
    score = 0
    while loop == True:
        
        snake.update()
        snake.go_forward()
        snake.detect_key()
        snake.detect_wall()
        if snake.head.distance(food.random_x,food.random_y) <15:
            scoreboard.change_score()
            snake.extend()
            food.new_position()
        if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
            print("You lost")
            scoreboard.lost()
            game_is_on=0
            loop=False
        if snake.check_collision()== 0:
            print("You lost")
            scoreboard.lost()
            game_is_on=0
            loop=False
        
screen.exitonclick()