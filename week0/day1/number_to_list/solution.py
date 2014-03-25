def number_to_list(n):
    lists = []
    the_list = []
    if n < 0:
        n = abs(n)
    while n > 0:
        digit = n % 10
        lists.append(digit)
        n = n // 10
    k = len(lists)
    while k > 0:
        k -= 1
        the_list.append(lists[k])
    return the_list
