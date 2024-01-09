from turtle import Turtle

CORDENATES = (0, -290)

class Net():
    def __init__(self):
        self.net_list = []
        self.create_nest()
        self.move()

    def create_nest(self):
        for _ in range(23):
            new_nest = Turtle()  
            new_nest.color("white")
            new_nest.shape('square')
            new_nest.shapesize(stretch_wid=0.2, stretch_len=0.6)
            self.net_list.append(new_nest)


    def move(self):  
        x = 0
        y = -250
        for index in range(len(self.net_list)):
            turtle_obj = self.net_list[index]
            turtle_obj.penup()
            turtle_obj.goto(x, y)
            turtle_obj.setheading(90)
            y = y + 23
            if index == len(self.net_list) - 1:
                print(turtle_obj.position())
