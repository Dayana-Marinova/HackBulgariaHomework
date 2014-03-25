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
