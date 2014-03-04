def magic_square(matrix):
	col_list_of_sum = []
	row_list_of_sum = []
	sum_of_diagonal1 = 0
	sum_of_diagonal2 = 0
	sum_of_col = 0
	sum_of_row = 0

	for row in matrix:
		for i in row:
			sum_of_row += i
		row_list_of_sum.append(sum_of_row)
		sum_of_row = 0
	#print row_list_of_sum

	first_row_sum = row_list_of_sum[0]
	for i in row_list_of_sum:
		if first_row_sum != i:
			return False

	for row in range(0,len(matrix)):
		for col in range(0,len(matrix)):
			sum_of_col += matrix[col][row]
		col_list_of_sum.append(sum_of_col)
		sum_of_col = 0
	#print col_list_of_sum
	
	first_col_sum = col_list_of_sum[0]
	for i in col_list_of_sum:
		if first_col_sum != i:
			return False

	if first_col_sum != first_row_sum:
		return False

	
	for col in range(0,len(matrix)):
		for row in range(0,len(matrix)):
			if row == col:
				sum_of_diagonal1 += matrix[col][row]
	#print sum_of_diagonal1


	for col in range(0,len(matrix)):
		for row in range(0,len(matrix)):
			if row == col:
				sum_of_diagonal2 += matrix[len(matrix)-1-row][row]
	#print sum_of_diagonal2

	if sum_of_diagonal2 != sum_of_diagonal1:
		return False

	if sum_of_diagonal1 != col_list_of_sum[0]:
		return False

	
	return True	

def main():
	print magic_square([[4,9,2], [3,5,7], [8,1,6]])
	print magic_square([[1,2,3], [4,5,6], [7,8,9]])
	print magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]])
	print magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]])
	print magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]])

if __name__ == '__main__':
	main()