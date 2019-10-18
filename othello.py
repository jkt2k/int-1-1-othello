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
def drawBoard():
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
def whichRow(y):
    return(int(8-((y+200)/50)))
def whichColumn(x):
    return(int((x+200)/50))
def xFromColumn(column):
    return((column*50)-175)
def yFromRow(row):
    return((row*-50)+175)
def stampPlayer(row, column, player):
    t.tracer(0,0)
    t.setpos(xFromColumn(column),yFromRow(row))
    t.dot(37,'green')
    t.dot(35, player)
    t.tracer(1,0)
def updateBoard(board,player,row,col):
    board[row][col]=player
    return board
def calculateScore(board,player):
    score=0
    for row in board:
        for col in row:
            if col==player:
                score+=1
    return score
def clearArea(x1,y1,x2,y2,color):
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
def updateScore(board,player):
    t.tracer(0,0)
    if player=="black":
        clearArea(-205,295,-50,270,'white')
        t.setpos(-200,270)
        t.write("black: "+str(calculateScore(board,"black")),font=("Arial", 20, "normal"))
        clearArea(-205, 245, -50, 220, 'white')
        t.setpos(-200, 220)
        t.write("white to move",font=("Arial", 20, "normal"))
    elif player=="white":
        clearArea(-205, 270, -50, 245, 'white')
        t.setpos(-200,245)
        t.write("white: " + str(calculateScore(board,"white")),font=("Arial", 20, "normal"))
        clearArea(-205, 245, -50, 220, 'white')
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
def sandwich(board,rowChange,columnChange,originalPlayer,previousRow,previousColumn,firstCheck,squaresInThisSequence):
    global squaresToBeReplaced
    if rowChange==-1 and previousRow==0 and firstCheck==False:
        return False
    elif rowChange==1 and previousRow==7 and firstCheck==False:
        return False
    elif columnChange==-1 and previousColumn==0 and firstCheck==False:
        return False
    elif columnChange==1 and previousColumn==7 and firstCheck==False:
        return False
    squareBeingChecked=board[previousRow+rowChange][previousColumn+columnChange]
    if squareBeingChecked==0:
        return False
    elif squareBeingChecked==originalPlayer and firstCheck==True:
        return False
    elif squareBeingChecked==originalPlayer and firstCheck==False:
        for square in squaresInThisSequence:
            squaresToBeReplaced.append(square)
        return True
    else:
        squaresInThisSequence.append([previousRow + rowChange, previousColumn + columnChange])
        return sandwich(board,rowChange,columnChange,originalPlayer,previousRow+rowChange,previousColumn+columnChange,False,squaresInThisSequence)
def validMove(board,player,row,column):
    moveIsValid=False
    if row not in range(0,8):
        return False
    if column not in range(0,8):
        return False
    if board[row][column]!=0:
        return False
    compass=[[0,0,0],[0,'null',0],[0,0,0]]
    for layer in range(0,len(compass)):
        for dir in range(0,len(compass)):
            if row==0 and layer==0:
                compass[layer][dir]='null'
            elif column==0 and dir==0:
                compass[layer][dir]='null'
            elif row == 7 and layer == 2:
                compass[layer][dir] = 'null'
            elif column == 7 and dir == 2:
                compass[layer][dir] = 'null'
    for layer in range(0,len(compass)):
        for dir in range(0,len(compass)):
            if compass[layer][dir]!='null':
                if not board[row+layer-1][column+dir-1]==0:
                    if sandwich(board,layer-1,dir-1,player,row,column,True,[])==True:
                        moveIsValid=True
    if moveIsValid==True:
        return True
    else:
        return False
def allMoves(board,player):
    validMoves=[]
    for row in range(0,len(board)):
        for square in range(0,len(board[row])):
            if validMove(board,player,row,square)==True:
                validMoves.append([row,square])
    return validMoves
def nextBoard(board,player,move):
    result=deepcopy(board)
    result[move[0]][move[1]]=player
    return result
def eatTheSandwich():
    return 1
def inputHandler(x,y):
    global whoseTurn
    global squaresToBeReplaced
    global move
    if whoseTurn == 'black':
        otherPlayer = 'white'
    else:
        otherPlayer = 'black'
    squaresToBeReplaced=[]
    row=whichRow(y)
    column=whichColumn(x)
    if column in range(0,8) and row in range(0,8) and validMove(gameBoard,whoseTurn,row,column)==True:
        move+=1
        gameBoard[row][column]=whoseTurn
        stampPlayer(row,column,whoseTurn)
        for square in squaresToBeReplaced:
            gameBoard[square[0]][square[1]]=whoseTurn
            stampPlayer(square[0],square[1],whoseTurn)
        calculateScore(gameBoard,'black')
        calculateScore(gameBoard,'white')
        if move==60:
            blackTotal=0
            whiteTotal=0
            for row in gameBoard:
                for square in row:
                    if square=='black':
                        blackTotal+=1
                    else:
                        whiteTotal+=1
            t.tracer(0,0)
            t.setpos(50, 220)
            if blackTotal>whiteTotal:
                t.write('black wins', font=("Arial", 20, "normal"))
            elif whiteTotal>blackTotal:
                t.write('white wins', font=("Arial", 20, "normal"))
            else:
                t.write('draw', font=("Arial", 20, "normal"))
            t.tracer(1,0)
        if len(allMoves(gameBoard,otherPlayer))!=0:
            updateScore(gameBoard, otherPlayer)
            updateScore(gameBoard, whoseTurn)
            whoseTurn=otherPlayer
        else:
            updateScore(gameBoard,whoseTurn)
            updateScore(gameBoard,otherPlayer)