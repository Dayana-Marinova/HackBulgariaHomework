from contains_digit import contains_digit


def contains_digits(number, digits):
    for i in digits:
        dig = contains_digit(number, i)
        if not dig:
            return False
    return True
