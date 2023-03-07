#!/usr/bin/python3
# Everett Reynolds
# Artificial Life
import math
from math import sqrt 
import sys
import random

class lifeCell:
    def __init__(game,state,neighbors,age):
        game.state = state
        game.neighbors = neighbors
        game.age = age


def randomGame():
    print("random")
    board = []
    boardSize = 0
    numSims = 0
    boardMaker(board,boardSize,numSims)
    #numSims = boardMaker(board,boardSize,numSims)
    #print(boardSize)
    numSims = int(input("How many generations would you like to run through in this board configuration? 1-100."))
    print(numSims)
    print("Here's the Initial Colony.")
    boardPrinter(board)
    neighbors(board)
    nextGen(board)
    for x in range(1, numSims):
        print("Here is Generation " + str(x+1))
        neighbors(board)
        nextGen(board)
        boardPrinter(board)

def customGame(file):
    print("custom")

def help():
    print(" Your Input Was Incorrect.\n Here's how to use the Game of Life. \n If There are no flags or files input, a random colony will be generated. \n If a '-f' with a filename is inputted, there file is the initial grid setup.")

def boardMaker(board,boardSize,numSims):
    size = 20
    print("Welcome to The Game of Life!\nThe Rules of The Game are as Follows..\nEach cell with one or no neighbors will die of loneliness.\nA cell with four or more neighbors dies of overpopulation.\nA cell with 2 or 3 neighbors will survive.\nAny cell over 10 generations old will die of old age.\n")
    #size = input("How large is your initial population? (How many initial cells should be populated (< 200) ).")

    for x in range(0,201):
        cell = lifeCell(state=0,neighbors=2,age=0)
        rand = random.randint(0,100)
        if((rand % 10) < 6):
            cell.state = 'X'
        else:
            cell.state = '0'
        cell.age = 0
        board.append(cell)

def boardPrinter(board):
    size = math.sqrt(len(board))
    count = 0
    #str = ""
    for x in range(0,200):
        count = count +1
        if(count % 21 == 0):
            print("\n")
        
        print(board[count].state)
        print(count)
        #print(' '.join(map(str,board[count].state)))
def neighbors(board):
    size = 200
    appSize = int(sqrt(200))
    for x in range(len(board)):
        n = [0,0,0,0,0,0,0,0]
        if x == 0:
            n[0] = board[1].state
            n[1] = board[size].state
            n[2] = board[appSize+1].state
        elif x == (size-1):
            n[0] = board[size-appSize-2].state
            n[1] = board[size-appSize-1].state
           # n[2] = board[2*size-2].state
        elif x == (size - 1):
            n[0] = board[size-2].state
            n[1] = board[2*size-2].state
            n[2] = board[2*size-1].state
        elif x == (size - appSize):
            n[0] = board[size-appSize+1].state
            n[1] = board[size-(2*appSize)].state
            n[2] = board[size-(2*appSize)+1].state
        elif x >= 1 and x <= (appSize-2):
            n[0] = board[x+1].state
            n[1] = board[x-1].state
            n[2] = board[x+appSize+1].state
            n[3] = board[x+appSize].state
            n[4] = board[x+appSize+1].state
        elif x > 0 and (x % appSize == 0):
           # n[0] = board[x+appSize].state
            n[1] = board[x-appSize].state
            #n[2] = board[x+appSize+1].state
            n[3] = board[x-appSize+1].state
            n[4] = board[x+1].state
        elif x > appSize-1 and (x+1)% appSize == 0:
            #n[0] = board[x+appSize].state
            n[1] = board[x-appSize].state
            #n[2] = board[x+appSize-1].state
            n[3] = board[x-appSize-1].state
            n[4] = board[x-1].state
        else:
            #n[0] = board[x+1].state
            n[1] = board[x-1].state
            #n[2] = board[x+appSize-1].state
            n[3] = board[x-appSize+1].state
            #n[4] = board[x+appSize].state
            n[5] = board[x-appSize].state
            #n[6] = board[x+appSize+1].state
            n[7] = board[x-appSize-1].state
        board[x].neighbors = n

           

    #print("neighbors")

def nextGen(board):
    dummyBoard = board
    for x in range(len(dummyBoard)):
        live = 0
        
        for y in range(7):
            if dummyBoard[x].neighbors[y] == 'X':
                live = live + 1
        if live == 0 or live == 1 or live >= 4:
            dummyBoard[x].state = "0"
            dummyBoard[x].age = 0
        elif live == 2:
            dummyBoard[x] = board[x]
        elif live == 3:
            if(dummyBoard[x].state == "0"):
                dummyBoard[x].state = "X"
                dummyBoard[x].age = 0
        if(dummyBoard[x].age == 9):
            dummyBoard[x].state = "0"
            dummyBoard[x].age = 0
        else:
            dummyBoard[x].age = dummyBoard[x].age + 1
    board = dummyBoard
    #print("next")







file = ""
#board = []
argNum = 0
argNum = len(sys.argv)
#print(argNum)
if argNum == 1:
    randomGame()
if argNum == 2:
    help()   
if argNum == 3:
    if sys.argv[1] == "-f":
        file = sys.argv[2]
        customGame(file)
    else:
        help()
if argNum < 1 or argNum >  3 :
    help()









