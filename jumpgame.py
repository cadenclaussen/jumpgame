import time
import random	


def main():
	score = 0
	board = generateBoard()
	printBoard(board)
	score = runGame(board, score)
	print("You got: " + str(score))

def printBoard(board):
	for _ in range(40):
		print("_", end="")

	print('')

	for y in range(7):
		for x in range(40):
			print(board[y][x], end="")
		print("|")
	

def generateBoard():
	board = []
	for _ in range(4):
		board.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
	board.append(["D", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
	board.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
	board.append(["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
	return board

def runGame(board, score):
	while True:
		board = updateBoard(board, board[4].index("D"))
		if board == False:
			print("Game Over...")
			return score
		printBoard(board)
		time.sleep(0.1)
		score += 40

def updateBoard(board, dindex):
	board[4][dindex] = "_"
	if dindex == 38:
		board[4][0] = "D"
		newList = new4Board()
		board[4] = newList
	else:
		if board[4][dindex + 1] == "C":
			return False
		else:
			board[4][dindex + 1] = "D"
	return board

def new4Board():
	newList = ["D", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
	for _ in range(10):
		newList[random.randint(3, 38)] = "C"
	return newList




main()
