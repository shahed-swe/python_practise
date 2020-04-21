from random import *
from turtle import *
from base import vector #our self made vector class

def value():
    # this || generate value from [-5,-3] to [3,5]
    return (3+random()*2)*choice([-1,1])


ball = vector(0,0)
aim = vector(value(),value())

# the projection or movement
def draw():
    # move the ball and draw the screen for us
    ball.move(aim)
    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x
    elif y < -200 or y > 200:
        aim.y = -aim.y
    clear()
    goto(x,y)
    dot(10,'green')
    ontimer(draw,20)

setup(420,420,370,0)
hideturtle()
tracer(False)
up() #draw moving to the up
draw()
done()
