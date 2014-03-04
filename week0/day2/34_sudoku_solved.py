def sudoku_solved(sudoku):
	dictionary = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
	for row in sudoku:
		for i in row:
			dictionary[i] += 1
		for num in dictionary:
			if dictionary[num] != 1:
				return False
				dictionary[num] = 0
			else:
				dictionary[num] = 0


	for row in range(0,len(sudoku)):
		for col in range(0,len(sudoku)):
			dictionary[sudoku[col][row]] += 1
		for num in dictionary:
			if dictionary[num] != 1:
				return False
			else:
				dictionary[num] = 0

	# purvoto kvadrat4e
	for row in range(0,len(sudoku)/3):
		for col in range(0,len(sudoku)/3):
			dictionary[sudoku[row][col]] += 1
	#print dictionary
	for num in dictionary:
		if dictionary[num] != 1:
			print False
		else:
			dictionary[num] = 0

	# srednoto
	for row in range(3,len(sudoku)-3):
		for col in range(3,len(sudoku)-3):
			dictionary[sudoku[row][col]] += 1
	#print dictionary
	for num in dictionary:
		if dictionary[num] != 1:
			return False
		else:
			dictionary[num] = 0

	#poslednoto
	for row in range(6,len(sudoku)):
		for col in range(6,len(sudoku)):
			dictionary[sudoku[row][col]] += 1
	#print dictionary
	for num in dictionary:
		if dictionary[num] != 1:
			return False
		else:
			dictionary[num] = 0

	for row in range(3,len(sudoku)-3):
		for col in range(0,len(sudoku)/3):
			dictionary[sudoku[row][col]] += 1
			dictionary[sudoku[col][row]] += 1
	#print dictionary
	for num in dictionary:
		if dictionary[num] != 2:
			return False
		else:
			dictionary[num] = 0


	for row in range(6,len(sudoku)):
		for col in range(0,len(sudoku)/3):
			dictionary[sudoku[row][col]] += 1
			dictionary[sudoku[col][row]] += 1
	#print dictionary
	for num in dictionary:
		if dictionary[num] != 2:
			return False
		else:
			dictionary[num] = 0

	for row in range(3,len(sudoku)-3):
		for col in range(6,len(sudoku)):
			dictionary[sudoku[row][col]] += 1
			dictionary[sudoku[col][row]] += 1
	#print dictionary
	for num in dictionary:
		if dictionary[num] != 2:
			return False
		else:
			dictionary[num] = 0



	return True
def main():		
	print sudoku_solved([
	[4, 5, 2, 3, 8, 9, 7, 1, 6],
	[3, 8, 7, 4, 6, 1, 2, 9, 5],
	[6, 1, 9, 2, 5, 7, 3, 4 ,8],
	[9, 3, 5, 1, 2, 6, 8, 7, 4],
	[7, 6, 4, 9, 3, 8, 5, 2, 1],
	[1, 2, 8, 5, 7, 4, 6, 3, 9],
	[5, 7, 1, 8, 9, 2, 4, 6, 3],
	[8, 9, 6, 7, 4, 3, 1, 5 ,2],
	[2, 4, 3, 6, 1, 5, 9, 8, 7]
	])

	print sudoku_solved([
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
	])

	print sudoku_solved([
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[2, 2, 2, 2, 2, 2, 2, 2, 2],
	[3, 3, 3, 3, 3, 3, 3, 3, 3],
	[4, 4, 4, 4, 4, 4, 4, 4, 4],
	[5, 5, 5, 5, 5, 5, 5, 5, 5],
	[6, 6, 6, 6, 6, 6, 6, 6, 6],
	[7, 7, 7, 7, 7, 7, 7, 7, 7],
	[8, 8, 8, 8, 8, 8, 8, 8, 8],
	[9, 9, 9, 9, 9, 9, 9, 9, 9]
	])

if __name__ == '__main__':
	main()