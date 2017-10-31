import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.special import binom
#%matplotlib inline
winnerList = []

def randomRoll(ran):
    #print("Rolling")
    random = np.random.randint(ran)
    return random

def turn(player, board, ):
    placed = False
    if(board[0] != 0 and board[1] != 0 and board[2] != 0 and board[3] != 0 and board[4] != 0 and board[5] != 0 and board[6] != 0 and board[7] != 0 and board[8] != 0):
        return True, board

    if(player == 'X'):
        #print("turn X")
        while(placed == False):
            random = randomRoll(8)
            if(board[random] == 0):
                board[random] = 'X'
                placed = True
        return False, board
    
    if(player == 'Y'):
        #print("turn Y")
        while(placed == False):
            random = randomRoll(8)
            if(board[random] == 0):
                board[random] = 'Y'
                placed = True
        return False, board


def winCondition(board, winnerList):
    playerWins = False
    #print("winCondition")
    
    if(board[0] == board[1] and board[1] == board[2] and board[0] != 0):
        win = board[0]
        winnerList.append(win)
        playerWins = True
    elif(board[3] == board[4] and board[4] == board[6] and board[3] != 0):
        win = board[3]
        winnerList.append(win)
        playerWins = True
    elif(board[6] == board[7] and board[7] == board[8] and board[6] != 0):
        win = board[6]
        winnerList.append(win)
        playerWins = True
    elif(board[6] == board[3] and board[3] == board[0] and board[6] != 0):
        win = board[6]
        winnerList.append(win)
        playerWins = True
    elif(board[7] == board[4] and board[4] == board[1] and board[7] != 0):
        win = board[7]
        winnerList.append(win)
        playerWins = True
    elif(board[8] == board[5] and board[5] == board[2] and board[8] != 0):
        win = board[8]
        winnerList.append(win)
        playerWins = True
    elif(board[6] == board[7] and board[7] == board[8] and board[6] != 0):
        win = board[6]
        winnerList.append(win)
        playerWins = True
    elif(board[6] == board[4] and board[4] == board[2] and board[6] != 0):
        win = board[6]
        winnerList.append(win)
        playerWins = True
    elif(board[0] == board[4] and board[4] == board[8] and board[0] != 0):
        win = board[0]
        winnerList.append(win)
        playerWins = True
    return playerWins, winnerList
    
def tic_tac_toe(games):
    board = [0] * 9
    winnerList = []
    for i in range(0,games):
        #print("game running")
        playerWins = False
        while(playerWins == False):
            playerWins, winnerList = winCondition(board, winnerList)
            exitGame, board = turn('Y', board)
            exitGame, board = turn('X', board)
            print(winnerList)

tic_tac_toe(1)