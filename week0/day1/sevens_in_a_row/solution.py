def sevens_in_a_row(arr, n):
    num = 0
    if not 7 in arr and n == 0:
        return True
    for i in range(0, len(arr)):
        if arr[i] == 7:
            num += 1
            if num == n:
                return True
        else:
            num = 0
    return False


def main():
    print sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3)
    print sevens_in_a_row([1, 7, 1, 7, 7], 4)
    print sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3)
    print sevens_in_a_row([7, 2, 1, 6, 2], 1)
    print sevens_in_a_row([10, 2, 1, 6, 2], 0)

if __name__ == '__main__':
    main()
