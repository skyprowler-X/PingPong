from turtle import Turtle


class Score(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score_player = 0
        self.penup() 
        self.color("white")
        self.hideturtle()
        self.set_score_localization(x_pos, y_pos)
        

    def set_score_localization(self, x_pos, y_pos):
        self.goto(x_pos, y_pos)
        self.write("0" , align="center", font=('Courier', 50, 'normal'))

    def update_score(self):    
        self.clear()   
        self.score_player += 1
        self.write(f"{self.score_player}" , align="center", font=('Courier', 50, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER" , align="center", font=('Courier', 50, 'normal'))
        