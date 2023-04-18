import turtle
import random

s = turtle.getscreen()
s.bgcolor("lightblue")

p1 = turtle.Turtle()
p1.speed(100)
p2 = p1.clone()

# setting the turtles and put them at their position
p1.color("red")
p1.shape("turtle")
p1.penup()
p1.goto(-200, 100)

p2.color("blue")
p2.shape("turtle")
p2.penup()
p2.goto(-200, -100)

# make the finish for both

p1.goto(300, 60)
p1.pendown()
p1.circle(40)
p1.penup()
p1.goto(-200, 100)

p2.goto(300, -140)
p2.pendown()
p2.circle(40)
p2.penup()
p2.goto(-200, -100)

# creating the die
dice = [
    '\u2680',  # ⚀
    '\u2681',  # ⚁
    '\u2682',  # ⚂
    '\u2683',  # ⚃
    '\u2684',  # ⚄
    '\u2685'  # ⚅
]

# create the game
p1.speed(1)
p2.speed(1)
for i in range(20):
    if p1.pos() >= (300, 100):
        print("Player 1 Win !")
        break
    elif p2.pos() >= (300, -100):
        print("Player 2 Win !")
        break

    else:
        enter_p1 = input("Player 1 'Enter' to roll the die !")
        die_outcome = random.choice(range(1, 7))
        print(f"You got :{dice[die_outcome-1]}")
        print(f"You move {die_outcome * 20} point")
        p1.fd(die_outcome * 20)

        enter_p2 = input("Player 2 'Enter' to roll the dice !")
        die_outcome = random.choice(range(1, 7))
        print(f"You got {dice[die_outcome - 1]}")
        print(f"You move {die_outcome * 20} points")
        p2.fd(die_outcome * 20)
