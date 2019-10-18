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
def which_row(y):
    return(int(8-((y+200)/50)))
def which_column(x):
    return(int((x+200)/50))
def x_from_column(column):
    return((column*50)-175)
def y_from_row(row):
    return((row*-50)+175)
def stamp_player(row, column, player):
    t.tracer(0,0)
    t.setpos(x_from_column(column),y_from_row(row))
    t.dot(37,'green')
    t.dot(35, player)
    t.tracer(1,0)
def update_board(board,player,row,col):
    board[row][col]=player
    return board
def calculate_score(board,player):
    score=0
    for row in board:
        for col in row:
            if col==player:
                score+=1
    return score