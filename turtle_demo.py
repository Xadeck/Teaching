import turtle
import math

turtle.getscreen()

t = turtle.Turtle()

# We are going to look at recursion


def tree(t, length, angle, depth):
    t.forward(length)
    if depth == 1:
        return
    # Save position and orientation
    p = t.pos()
    h = t.heading()
    # Draw a left tree
    t.left(angle)
    tree(t, 0.8 * length, 1.1 * angle, depth - 1)
    t.setpos(p)
    t.setheading(h)
    # Draw a right tree
    t.right(angle)
    tree(t, 0.8 * length, 1.1 * angle, depth - 1)
    t.setpos(p)
    t.setheading(h)

t.setheading(90)
tree(t, 50, 15, 6)

turtle.done()

radius = 30
nb_triangles = 20
angle_deg = 360. / nb_triangles
angle_rad = angle_deg * 180. / math.pi
length = 2 * math.sin(angle_rad / 2.) * radius

t.speed(0)

for c in range(10):
    for n in range(nb_triangles):
        t.forward(length)
        t.left(angle_deg)
    t.right(360 / 10)

turtle.done()

