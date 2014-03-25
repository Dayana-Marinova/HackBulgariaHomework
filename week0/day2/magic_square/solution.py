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

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
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

    for col in range(0, len(matrix)):
        for row in range(0, len(matrix)):
            if row == col:
                sum_of_diagonal1 += matrix[col][row]
    #print sum_of_diagonal1

    for col in range(0, len(matrix)):
        for row in range(0, len(matrix)):
            if row == col:
                sum_of_diagonal2 += matrix[len(matrix) - 1 - row][row]
    #print sum_of_diagonal2

    if sum_of_diagonal2 != sum_of_diagonal1:
        return False

    if sum_of_diagonal1 != col_list_of_sum[0]:
        return False

    return True
