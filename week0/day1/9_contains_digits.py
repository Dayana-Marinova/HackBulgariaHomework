from contains_digit import contains_digit


def contains_digits(number, digits):
    for i in digits:
        dig = contains_digit(number, i)
        if not dig:
            return False
    return True


def main():
    print contains_digits(12345, [1, 2, 3])
    print contains_digits(402123, [0, 3, 4])
    print contains_digits(666, [6, 4])
    print contains_digits(123456789, [1, 2, 3, 0])
    print contains_digits(456, [])

if __name__ == '__main__':
    main()
