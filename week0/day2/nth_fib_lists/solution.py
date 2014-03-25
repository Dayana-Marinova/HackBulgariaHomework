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
