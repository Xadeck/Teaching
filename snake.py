from turtle import *
import turtle
import random
import time


# Define moving functions
def move_up():
    if head.direction != "down":
        head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_right():
    if head.direction != "left":
        head.direction = "right"


def move_left():
    if head.direction != "right":
        head.direction = "left"


# Define the function that will make the segments of the snake
def snake_segments(segments):

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


def check_colision():
    for segment in segments:
        if head.distance(segment) < 20:
            return True
    return False


def game_over():
    head.speed(0)
    head.goto(0, 0)
    head.direction = "stop"
    i = 0
    time.sleep(1)
    screen.clear()
    segments = []
    screen.bgcolor("light blue")
    points.goto(0, 0)
    points.write("GAME OVER", font=style, align="center")


def update_game():

    global i

    head.speed(2)
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if check_colision():
        game_over()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over()

    if head.distance(fruit) < 20:
        body = Turtle()
        body.shape("square")
        body.color("blue")
        body.speed(2)
        body.penup()
        segments.append(body)

        fruit.goto(random.randint(-290, 290), random.randint(-290, 290))

        points.clear()
        i += 1
        points.write(f"Points : {i}", font=style, align="center")

    snake_segments(segments)
    screen.update()
    screen.ontimer(update_game, 50)


# Creating the Screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgpic("pixel-green.gif")
screen.title("Snake Game")
screen.tracer(0)


# Creating the fruit
fruit = turtle.Turtle()
fruit.shape("circle")
fruit.color("red")
fruit.speed(0)
fruit.penup()
fruit.goto(30, 30)


# Creating the points text
points = turtle.Turtle()
style = ("Arial", 30, "normal")
points.penup()
points.speed(0)
points.goto(0, 200)
points.pendown()
i = 0
points.hideturtle()
points.write(f"Points : {i}", font=style, align="center")


screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Creating the head
head = turtle.Turtle()
head.color("blue")
head.speed(2)
head.shape("square")
head.penup()
head.direction = "stop"

segments = []
update_game()
turtle.done()
