from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,begin):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        if begin == "left":
            self.goto(-360,0)
        else:
            self.goto(360,0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() < 280:
            y_ = self.ycor() + 20
            self.goto(self.xcor(), y_)

    def go_down(self):
        if self.ycor() > -280:
            y_ = self.ycor() - 20
            self.goto(self.xcor(), y_)