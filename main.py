from turtle import Turtle, Screen

screen = Screen()
screen.title("Etch-a-sketch")

t = Turtle()


def forward():
    t.forward(10)


def backward():
    t.backward(10)


def left():
    t.left(10)


def right():
    t.right(10)


def clear():
    t.clear()
    t.reset()


screen.listen()
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
