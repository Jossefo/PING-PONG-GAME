from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score =0
        self.left_score =0
        self.show_points()

    def right_goal (self):
        self.left_score+=1
        self.clear()
        self.show_points()
    def left_goal (self):
        self.right_score+=1
        self.clear()
        self.show_points()


    def show_points(self):
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))
