def nth_fib_lists(listA, listB, n):
    new_list = []
    if n == 1:
        return listA
    if n == 2:
        return listB
    for i in range(1, n):
        new_list = listA + listB
        listA = listB
        listB = new_list
    return new_list


def main():
    print nth_fib_lists([1, 2, 3], [4, 5, 6], 1)
    print nth_fib_lists([1, 2, 3], [4, 5, 6], 2)
    print nth_fib_lists([1, 2, 3], [4, 5, 6], 3)
    print nth_fib_lists([1, 2, 3], [4, 5, 6], 4)

    print nth_fib_lists([1, 2], [3, 4], 4)
    print nth_fib_lists([1, 2], [3, 4], 5)
    print nth_fib_lists([], [], 100)

if __name__ == '__main__':
    main()
