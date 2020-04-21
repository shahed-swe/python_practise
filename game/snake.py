from turtle import *
from random import *
from tkinter import messagebox
from base import square,vector

food = vector(0,0) #food position
snake = [vector(10,0)] #snake position
aim = vector(0,-10)

def change(x,y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        # if snake eat it's own body
        square(head.x, head.y,9,'red')
        update()
        messagebox.showinfo("End","Game Over! Please Try Again")
        bye()

    snake.append(head)
    if head == food:
        # if snake eats the food here
        print(f"Snake: {len(snake)}")
        food.x = randrange(-15,15) * 10
        food.y = randrange(-15,15) * 10
        print(f"{food.x} -- {food.y}")
    else:
        snake.pop(0)
    clear() #clear the console
    for body in snake:
        square(body.x,body.y,9,'black')
        print(f"{body.x} -- {body.y}")
    square(food.x, food.y,9,'green')
    update()
    ontimer(move,100)

if __name__ == '__main__':
    setup(420,420,370,0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda:change(10,0),'Right')
    onkey(lambda:change(-10,0),'Left')
    onkey(lambda:change(0,10),'Up')
    onkey(lambda:change(0,-10),'Down')
    move()
    done()