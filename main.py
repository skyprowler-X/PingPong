import turtle as t
from player_paddle import Paddle
import time
from ball_pong import Ball
from scoreboard_help import Score
from middle_net_help import Net

POSITION_SCORE_PLAYERS = ((-50, 200), (50, 200))
START = True

screen = t.Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=800, height=600)


player_1 = Paddle(350, 0)
computer_2 = Paddle(-350, 0)
ball_obj = Ball()
score_player_1 = Score(50, 200)
score_computer = Score(-50, 200)
nest = Net()

screen.listen()
screen.onkeypress(player_1.pipe_player_up, "Up")
screen.onkeypress(player_1.pipe_player_down, "Down")
screen.onkeypress(computer_2.pipe_player_up, "w")
screen.onkeypress(computer_2.pipe_player_down, "s")




while START:   
    screen.update()
    time.sleep(ball_obj.move_speed)
    ball_obj.move()

    #detect collision with wall
    if ball_obj.ycor() >= 290 or ball_obj.ycor() <= -290:
        ball_obj.bounce_y()

    #detec collision with paddle
    if ball_obj.distance(player_1) < 50 and ball_obj.xcor() >= 330 or ball_obj.distance(computer_2) <= 50 and ball_obj.xcor() < -320:
        ball_obj.bounce_x()
        print(ball_obj.speed())     
        ball_obj.speed(10)
        print(ball_obj.speed())

    #detec computer  with paddle
    if ball_obj.xcor() > 400:
        ball_obj.start_again()
        score_computer.update_score()

    if ball_obj.xcor() < -400:
        ball_obj.start_again()    
        score_player_1.update_score()
        
        



    
    




screen.exitonclick()