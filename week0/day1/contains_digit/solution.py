def contains_digit(number, digit):
    if number < 0:
        number = abs(number)
    while number > 0:
        digits = number % 10
        if digits == digit:
            return True
        number = number // 10
    else:
        return False
