import turtle as t
import time
from copy import deepcopy
t.ht()
gameBoard=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
whoseTurn='black'
squaresToBeReplaced=[]
move=0
sec=0
t.setup(600,600)
t.pensize(5)
def draw_board():
    t.tracer(0,0)
    t.penup()
    t.setpos(-200,200)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    for i in range(0,4):
        t.forward(400)
        t.right(90)
    t.end_fill()
    for i in range(7):
        t.penup()
        t.setpos(-200,150-i*50)
        t.pendown()
        t.forward(400)
    t.right(90)
    for i in range(7):
        t.penup()
        t.setpos(-150+i*50,200)
        t.pendown()
        t.forward(400)
    t.penup()
    t.tracer(1,0)