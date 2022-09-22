from turtle import Turtle


class Mid(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-290)
        self.color("white")
        self.pensize(5)
        self.hideturtle()
        for i in range(60):
            self.dot(5, "white")
            self.fd(10)
