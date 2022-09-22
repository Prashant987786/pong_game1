from turtle import Screen

from score import Score

from ball import Ball
from midline import Mid
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(height=600, width=800)
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
mid = Mid()
score = Score()


screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bonce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bonce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
