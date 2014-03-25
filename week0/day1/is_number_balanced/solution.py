def is_number_balanced(n):
    saven = n
    digits = 0
    while n > 0:
        n = n // 10
        digits += 1
    dig = digits // 2
    dig1 = dig
    sum1 = 0
    sum2 = 0
    while dig > 0:
        sum1 += saven % 10
        saven = saven // 10
        dig -= 1
    if digits % 2 != 0:
        saven = saven // 10
    while dig1 > 0:
        sum2 += saven % 10
        saven = saven // 10
        dig1 -= 1
    if sum1 == sum2:
        return True
    return False
