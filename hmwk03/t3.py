import numpy as np
import pandas as pd
import random

def turn(player, board, remainingList):
	if(player == 'X'):
		choice = random.choice(remainingList)
		remainingList.remove(choice)
		board[choice] = 'X'
	if(player == 'Y'):
		choice = random.choice(remainingList)
		remainingList.remove(choice)
		board[choice] = 'Y'
	return remainingList, board
def selectWinner(board, winnerList):
    if(board[0] == board[1] and board[1] == board[2] and board[0] != 0):
        win = board[0]
        winnerList.append(win)
        return True, winnerList
    elif(board[3] == board[4] and board[4] == board[6] and board[3] != 0):
        win = board[3]
        winnerList.append(win)
        return True, winnerList
    elif(board[6] == board[7] and board[7] == board[8] and board[6] != 0):
        win = board[6]
        winnerList.append(win)
        return True, winnerList
    elif(board[6] == board[3] and board[3] == board[0] and board[6] != 0):
        win = board[6]
        winnerList.append(win)
        return True, winnerList
    elif(board[7] == board[4] and board[4] == board[1] and board[7] != 0):
        win = board[7]
        winnerList.append(win)
        return True, winnerList
    elif(board[8] == board[5] and board[5] == board[2] and board[8] != 0):
        win = board[8]
        winnerList.append(win)
        return True, winnerList
    elif(board[6] == board[7] and board[7] == board[8] and board[6] != 0):
        win = board[6]
        winnerList.append(win)
        return True, winnerList
    elif(board[6] == board[4] and board[4] == board[2] and board[6] != 0):
        win = board[6]
        winnerList.append(win)
        return True, winnerList
    elif(board[0] == board[4] and board[4] == board[8] and board[0] != 0):
        win = board[0]
        winnerList.append(win)
        return True, winnerList
    return False, winnerList

def game(trials):
	board = [0,0,0,0,0,0,0,0,0]
	selection = [0,1,2,3,4,5,6,7,8]
	winnerList = []

	for i in range(trials):
		board = [0]*9
		selection = [0,1,2,3,4,5,6,7,8]
		while(len(selection) != 0):
			selection, board = turn('X', board, selection)
			if(len(selection) == 0):
				break
			selection, board = turn('Y', board, selection)
			playerWins, winnerList = selectWinner(board, winnerList)
			if(playerWins == True):
				break
	print(winnerList)
	count = 0
	for i in winnerList:
		count += 1
	print(count/trials)
	
game(100)