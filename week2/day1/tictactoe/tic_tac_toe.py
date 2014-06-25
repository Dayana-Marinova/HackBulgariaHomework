def make_table():
    table = []
    for i in range(0, 3):
        table.append(["_"] * 3)
    return table


def print_table(table):
    for row in table:
        print(" ".join(row))


def play(table):
    print_table(table)
    while True:
        first_row = int(input('Enter the row:'))
        first_col = int(input('Enter the col:'))
        if first_row <= 2 and first_row >= 0 and first_col <= 2 and first_col >= 0:
            table[first_row][first_col] = "X"
            print_table(table)
        else:
            print('must awake greater than -1 and less than 3')
        if who_win(table):
            break
        second_row = int(input('Enter the row:'))
        second_col = int(input('Enter the col:'))
        if second_row <= 2 and second_row >= 0 and second_col <= 2 and second_col >= 0:
            table[second_row][second_col] = "O"
            print_table(table)
        else:
            print('must awake greater than -1 and less than 3')
        if who_win(table):
            break


def who_win(table):
    col_array_for_X = []
    col_array_for_X_first = []
    col_array_for_X_second = []
    diagonal_X = []
    col_array_for_O = []
    col_array_for_O_first = []
    col_array_for_O_second = []
    diagonal_O = []
    helpfull_array = []
    for item in table:
        if '_' not in item:
            helpfull_array.append(True)
    for row in range(0, len(table)):
        if table[row][0] == 'X':
            col_array_for_X.append(True)
        elif table[row][1] == 'X':
            col_array_for_X_first.append(True)
        elif table[row][2] == "X":
            col_array_for_X_second.append(True)
    for row in range(0, len(table)):
        if table[row][0] == 'O':
            col_array_for_O.append(True)
        elif table[row][1] == 'O':
            col_array_for_O_first.append(True)
        elif table[row][2] == "O":
            col_array_for_O_second.append(True)
    if table[0][0] == table[1][1] and table[2][2] == table[1][1] and table[1][1] == 'X':
        diagonal_X.append(True)
    elif table[0][2] == table[1][1] and table[2][0] == table[1][1] and table[1][1] == 'X':
        diagonal_X.append(True)
    elif table[0][0] == table[1][1] and table[2][2] == table[1][1] and table[1][1] == 'O':
        diagonal_O.append(True)
    elif table[0][2] == table[1][1] and table[2][0] == table[1][1] and table[1][1] == 'O':
        diagonal_O.append(True)
    if ['X', 'X', 'X'] in table:
        return 'X wins'
    elif ['O', 'O', 'O'] in table:
        return 'O wins'
    elif len(col_array_for_X) == 3 or len(col_array_for_X_first) == 3 and len(col_array_for_X_second) == 3:
        return 'X wins'
    elif len(col_array_for_O) == 3 or len(col_array_for_O_first) == 3 and len(col_array_for_O_second) == 3:
        return 'O wins'
    elif len(diagonal_X) == 1:
        return 'X wins'
    elif len(diagonal_O) == 1:
        return 'O wins'
    elif len(helpfull_array) == 3:
        return 'nobody wins'
    return False

#play(make_table())

#    def main():
#        print(play(make_table()))


#    if __name__ == '__main__':
#        main()
