from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


###########################################################################################
def main_flow(WIDTH: int = 800, HEIGHT: int = 600) -> bool:
    """

    :param WIDTH:
    :param HEIGHT:
    :return:
    """
    """ create screen """
    screen = Screen()
    screen.title("Ping Pong Gong")
    screen.bgcolor("Black")
    screen.setup(width=WIDTH, height=HEIGHT)
    middle_line = Turtle()
    logger.debug(f"Screen size: {WIDTH, HEIGHT}")

    screen.tracer(0)  # shuts down the animation
    # drow middle line
    middle_line.pencolor("white")
    middle_line.penup()
    middle_line.goto(0, -500)
    middle_line.left(90)

    for i in range(100):
        middle_line.pendown()
        middle_line.forward(10)
        middle_line.penup()
        middle_line.forward(10)
    left_paddle = Paddle(begin="left")
    right_paddle = Paddle(begin="right")

    screen.listen()
    screen.onkey(fun=right_paddle.go_up, key="Up")
    screen.onkey(fun=right_paddle.go_down, key="Down")
    screen.onkey(fun=left_paddle.go_up, key="w")
    screen.onkey(fun=left_paddle.go_down, key="s")

    ball = Ball()
    score = Score()
    ball.speed("fastest")

    game_om = True
    while game_om:
        time.sleep(0.092)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
            ball.bounce_x()
        if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
            ball.bounce_x()
        if ball.xcor() > 380:
            score.right_goal()
            ball.goto(0, 0)
        if ball.xcor() < -380:
            ball.goto(0, 0)
            score.left_goal()

    screen.exitonclick()
    return True


if __name__ == '__main__':
    logger.info("started run")

    main_flow()
    logger.info("finished run")
