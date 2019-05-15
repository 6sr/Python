import turtle
turtle.shape("turtle")
turtle.width(1)

turtle.fd(100)
turtle.undo()

def square():
    for i in range(4):
        turtle.fd(100)      #turtle.forward(100)
        turtle.lt(90)       #tutle.left(90)

def rectangle():
    for i in range(2):
        turtle.fd(100)
        turtle.lt(90)
        turtle.fd(50)
        turtle.lt(90)

def circle(x):
    for i in range(int(360 / x)):
        turtle.fd(x)
        turtle.lt(x)

def hexagon():
    for _ in range(6):
        turtle.forward(100)
        turtle.left(60)

for _ in range (6):
    hexagon()
    circle(1)
    square()
    turtle.forward(100)
    turtle.right(60)

help(turtle.color)

square()

turtle.color("red")
rectangle()

turtle.colormode(255)
turtle.color(215, 100, 170)
circle(10)

timmy = turtle      #timmy variable now acts as turtle
timmy.rt(70)        #turtle.right(70)
timmy.bk(100)       #turtle.back(100)   or    turtle.backward(100)

turtle.penup()
turtle.pendown()

#Clearing turtle screen
#ws = turtle.Screen()
#ws.clear()
#    same as
#turtle.reset()

#to pause the turtle graphics window
#turtle.getscreen()._root.mainloop()    same as
#turtle.done()      same as
input()