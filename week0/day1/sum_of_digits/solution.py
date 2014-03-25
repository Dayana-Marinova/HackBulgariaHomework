def sum_of_digits(n):
    if n < 0:
        n = abs(n)
    m = 0
    while n > 0:
        digit = n % 10
        m += digit
        n = n // 10
    return m
