import turtle
def draw_spiral(radius):
    x = turtle.xcor()
    y = turtle.ycor()
    speed = 1
    while True:
        turtle.fd(speed)
        turtle.lt(10)
        speed += 0.1
        if turtle.distance(x,y) > radius:
            break
def square(r):
    x = turtle.xcor()
    y = turtle.ycor()
    speed  = 10
    while True:
        turtle.fd(speed)
        turtle.lt(90)
        speed += 5
        if turtle.distance(x,y) > r:
            break
square(500)
input()