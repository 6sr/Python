import turtle
def drawShape(n):
    for i in range(n):
        for j in range(i + 3):
            turtle.fd(100)
            turtle.lt(360 / (i + 3))
        turtle.penup()
        turtle.fd(100 + 50 * (i / 2 + 1))
        turtle.pendown()

def drawUsingFunc(n,a):     #passing fucntion turtle.lt as argument a
    for i in range(n):
        for j in range(i + 3):
            turtle.fd(100)
            a(360 / (i + 3))
        turtle.penup()
        turtle.fd(100 + 50 * (i / 2 + 1))
        turtle.pendown()

turtle.penup()
turtle.goto(-600,0)
turtle.pendown()

drawUsingFunc(6,turtle.lt)      #poassing turtle.lt as argument

input()
