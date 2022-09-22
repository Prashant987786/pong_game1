from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.goto(x, y)
        self.setheading(90)

    def up(self):
        self.fd(50)

    def down(self):
        self.bk(50)
