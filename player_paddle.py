from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos): 
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)

    def pipe_player_up(self):
        if self.ycor() <= 240:
            self.goto(self.xcor() ,self.ycor() + 30)

    def pipe_player_down(self):
        if self.ycor()  >= -240:
            self.goto(self.xcor() ,self.ycor() - 30)

