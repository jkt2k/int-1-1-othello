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
def clear_area(x1,y1,x2,y2,color):
    t.tracer(0,0)
    t.setpos(x1,y1)
    t.setheading(0)
    t.color(color)
    t.pensize(1)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in (0,1):
        t.forward(x2-x1)
        t.left(90)
        t.forward(y2-y1)
        t.left(90)
    t.end_fill()
    t.penup()
    t.color('black')
    t.tracer(1,0)
def update_score(board,player):
    t.tracer(0,0)
    if player=="black":
        clear_area(-205,295,-50,270,'white')
        t.setpos(-200,270)
        t.write("black: "+str(calculate_score(board,"black")),font=("Arial", 20, "normal"))
        clear_area(-205, 245, -50, 220, 'white')
        t.setpos(-200, 220)
        t.write("white to move",font=("Arial", 20, "normal"))
    elif player=="white":
        clear_area(-205, 270, -50, 245, 'white')
        t.setpos(-200,245)
        t.write("white: " + str(calculate_score(board,"white")),font=("Arial", 20, "normal"))
        clear_area(-205, 245, -50, 220, 'white')
        t.setpos(-200,220)
        t.write("black to move",font=("Arial", 20, "normal"))
    t.tracer(1,0)
def initialize():
    global gameBoard
    global move
    move=0
    drawBoard()
    stampPlayer(3,3,"white")
    gameBoard=(updateBoard(gameBoard,"white",3,3))
    stampPlayer(4,4,"white")
    gameBoard = (updateBoard(gameBoard, "white", 4, 4))
    stampPlayer(3,4,"black")
    gameBoard = (updateBoard(gameBoard, "black", 3, 4))
    stampPlayer(4,3,"black")
    gameBoard = (updateBoard(gameBoard, "black", 4, 3))
    updateScore(gameBoard,"black")
    updateScore(gameBoard,"white")