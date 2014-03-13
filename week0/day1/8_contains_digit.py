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


def main():
    print contains_digit(100001, 3)
    print contains_digit(123, 4)
    print contains_digit(42, 2)
    print contains_digit(1000, 0)
    print contains_digit(12346789, 5)

if __name__ == '__main__':
    main()
