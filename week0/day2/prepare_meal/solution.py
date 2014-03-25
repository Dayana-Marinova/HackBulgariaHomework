def prepare_meal(number):
    first_str = 'spam '
    second_str = 'and eggs'
    if number == 5:
        return 'eggs'
    for i in range(1, number):
        if 3 ** i <= number:
            new_str = first_str * i
            if 3 ** i == number:
                return new_str
    if number % 5 == 0 and number != 0:
        return new_str + second_str
    else:
        return "''"
