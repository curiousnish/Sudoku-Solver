def print_board(board):
	"""
	prints the board in a more traditional way
	:parameter : board : 2d list of values from 0 to 9
	:return : None
	"""

	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - - - -")
		for j in range(len(board[0])):
			if j % 3 == 0:
				print(" | ", end="")
			if j == 8:
				print(board[i][j], end="\n")
			else:
				print(str(board[i][j]) + " ", end="")


def find_empty(board):
	"""
	finds the empty values in the 2d list
	:parameter : board : with empty (0) entries
	:return : (row, col) both as int
	"""

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i,j)

	return None


def valid(board, pos, num):
	"""
	returns if the attempted move is valid
	:parameter : board : 2d list of values
	:parameter : pos : (row, col)
	:parameter : num : to be checked
	:return : bool
	"""

	#check row
	for i in range(0, len(board)):
		if board[pos[0]][i] == num and pos[1] != i:
			return False
	#check col
	for i in range(0, len(board)):
		if board[i][pos[1]] == num and pos[1] != i:
			return False

	#check box
	box_x = pos[1]//3
	box_y = pos[0]//3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3):
			if board[i][j] == num and (i,j) != pos:
				return False

	return True


def solver(board):
	"""
	solves soduko using backtracking algo
	:parameter : board : 2d list of values
	:return : solution
	"""

	find = find_empty(board)

	if find:
		row, col = find
	else:
		return True

	for i in range(1,10):
		if valid(board, (row, col), i):
			board[row][col] = i

			if solver(board):
				return True

			board[row][col] = 0

	return False



board = [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]
    ]

print_board(board)
solver(board)
print("///////////////////////////////")
print_board(board)