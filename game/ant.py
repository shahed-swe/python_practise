from random import *
from turtle import *
from base import vector #our self made vector class

ant = vector(0,0)
aim = vector(2,0)

def wrap(value):
    return value

def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    aim.move(random() - .5) #this is for dodging the dot up side
    # rotation
    aim.rotate(random() * 10 - 5)
    clear()
    # goto the pointer
    goto(ant.x,ant.y)
    dot(14, 'red')
    if running:
        ontimer(draw,100) #function calling time


setup(420,420,370,0)
hideturtle()
tracer(False)
up()
running = True
draw()
done()