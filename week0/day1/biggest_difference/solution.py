def biggest_difference(arr):
    max_num = arr[0]
    min_num = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
        elif arr[i] > max_num:
            max_num = arr[i]
    return min_num - max_num
