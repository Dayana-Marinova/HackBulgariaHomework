def member_of_nth_fib_lists(listA, listB, needle):
    new_list = []
    if needle == listA:
        return True
    if needle == listB:
        return True
    for i in range(2, len(needle)):
        new_list = listA + listB
        listA = listB
        listB = new_list
        if new_list == needle:
            return True
    else:
        return False
