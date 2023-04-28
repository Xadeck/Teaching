import turtle
import random

s = turtle.getscreen()
s.bgcolor("black")

# intialize list of house positions
houselist = []


# intialize the players
def initialize(player, color, position, speed):
    player.color(color)
    player.shape("turtle")
    player.penup()
    player.speed(speed)
    player.goto(position[0], position[1])
    pos = player.pos()
    player.fd(500)
    # save the house position
    housepos = player.pos()
    player.pendown()
    player.circle(40)
    player.penup()
    # bring the turtles back to their start position
    player.setpos(pos)
    # appending house positions in a list
    houselist.append(housepos)


colors = ("red", "blue", "orange", "purple", "green", "yellow")
first_position = (-200, 200)

players = [turtle.Turtle() for n in range(4)]
for i in players:
    initialize(i, random.choice(colors), first_position, 0)
    first_position = (first_position[0], first_position[1] - 100)


# create the die
dice = [
    '\u2680',  # ⚀
    '\u2681',  # ⚁
    '\u2682',  # ⚂
    '\u2683',  # ⚃
    '\u2684',  # ⚄
    '\u2685'  # ⚅
]

# create the game
game_over = False
while not game_over:
    for i in range(len(players)):
        player = players[i]
        housepos = houselist[i]
        if player.distance(housepos) < 50:
            print(f"Player {i+1} WIN !!! ")
            game_over = True
            break
        else:
            input(f"Player {i+1} roll the dice, press 'Enter'")
            dice_outcome = random.choice(range(1, 7))
            print(f"Player {i+1} got {dice[dice_outcome - 1]}")
            print(f"Player {i+1} move {dice_outcome * 20} points")
            player.fd(20 * dice_outcome)
