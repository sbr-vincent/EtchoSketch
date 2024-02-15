from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()


# Creating an etcho sketch
def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.right(180)
    tim.forward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def reset():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=reset)


screen.exitonclick()
