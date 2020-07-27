"""
here we have build a simple game by using turtle
"""
from random import *
from turtle import *

from base import vector

ball = vector(-200,-200)
speed = vector(0,0)
targets = []

def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

def tap(x,y):
    # respond to the screen
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def draw():
    # draw the ball and targets

    clear()
    for target in targets:
        goto(target.x, target.y)
        dot(20,'red')
    
    if inside(ball):
        goto(ball.x,ball.y)
        dot(6,'blue')
    
    update()


def move():
    # movement of ball and target 
    if  randrange(40) == 0:
        y = randrange(-150,150)
        target = vector(200,y)
        targets.append(target)
    
    for target in targets:
        target.x -= 0.5
        # print(target.x)
    
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
        print(f"{speed.y} --> {ball}")
    dupe = targets.copy()
    targets.clear()
    for target in dupe:
        if abs(target - ball) > 13:
            print(abs(target - ball))
            targets.append(target)
    draw()
        
    for target in targets:
        if not inside(target):
            return
    # ontimer(move, 50)
    ontimer(move,50)


setup(420,420,370,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
