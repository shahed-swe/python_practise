from turtle import *
from base import square,vector
from tkinter import messagebox


p1_xy = vector(-100,0)
p1_aim = vector(4,0)
p1_body = set()

p2_xy = vector(100,0)
p2_aim = vector(-4,0)
p2_body = set()

def inside(head):
    # return true if head inside boundary
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    p1_xy.move(p1_aim)
    p1_head = p1_xy.copy()
    p2_xy.move(p2_aim)
    p2_head = p2_xy.copy()

    if not inside(p1_head) or p1_head in p2_body:
        # print("player blue won")
        messagebox.showinfo("Winner","Blue Won this time")
        bye()
    
    if not inside(p2_head) or p2_head in p1_body:
        messagebox.showinfo("Winner","Red Won this time")
        bye()
    
    p1_body.add(p1_head)
    p2_body.add(p2_head)
    
    square(p1_xy.x,p1_xy.y,3,'red')
    square(p2_xy.x,p2_xy.y,3,'blue')
    update()
    ontimer(draw,50)

setup(420,420,370,0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1_aim.rotate(90),'a')
onkey(lambda: p1_aim.rotate(-90),'d')
onkey(lambda: p2_aim.rotate(90),'j')
onkey(lambda: p2_aim.rotate(-90),'l')
draw()
done()
