def sudoku_solved(sudoku):
    dictionary = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for row in sudoku:
        for i in row:
            dictionary[i] += 1
        for num in dictionary:
            if dictionary[num] != 1:
                return False
                dictionary[num] = 0
            else:
                dictionary[num] = 0

    for row in range(0, len(sudoku)):
        for col in range(0, len(sudoku)):
            dictionary[sudoku[col][row]] += 1
        for num in dictionary:
            if dictionary[num] != 1:
                return False
            else:
                dictionary[num] = 0

    # purvoto kvadrat4e
    for row in range(0, len(sudoku) / 3):
        for col in range(0, len(sudoku) / 3):
            dictionary[sudoku[row][col]] += 1
    #print dictionary
    for num in dictionary:
        if dictionary[num] != 1:
            return False
        else:
            dictionary[num] = 0

    # srednoto
    for row in range(3, len(sudoku) - 3):
        for col in range(3, len(sudoku) - 3):
            dictionary[sudoku[row][col]] += 1
    #print dictionary
    for num in dictionary:
        if dictionary[num] != 1:
            return False
        else:
            dictionary[num] = 0

    #poslednoto
    for row in range(6, len(sudoku)):
        for col in range(6, len(sudoku)):
            dictionary[sudoku[row][col]] += 1
    #print dictionary
    for num in dictionary:
        if dictionary[num] != 1:
            return False
        else:
            dictionary[num] = 0

    for row in range(3, len(sudoku) - 3):
        for col in range(0, len(sudoku) / 3):
            dictionary[sudoku[row][col]] += 1
            dictionary[sudoku[col][row]] += 1
    #print dictionary
    for num in dictionary:
        if dictionary[num] != 2:
            return False
        else:
            dictionary[num] = 0

    for row in range(6, len(sudoku)):
        for col in range(0, len(sudoku) / 3):
            dictionary[sudoku[row][col]] += 1
            dictionary[sudoku[col][row]] += 1
    #print dictionary
    for num in dictionary:
        if dictionary[num] != 2:
            return False
        else:
            dictionary[num] = 0

    for row in range(3, len(sudoku) - 3):
        for col in range(6, len(sudoku)):
            dictionary[sudoku[row][col]] += 1
            dictionary[sudoku[col][row]] += 1
    #print dictionary
    for num in dictionary:
        if dictionary[num] != 2:
            return False
        else:
            dictionary[num] = 0

    return True
