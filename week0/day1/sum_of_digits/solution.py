def sum_of_digits(n):
    if n < 0:
        n = abs(n)
    m = 0
    while n > 0:
        digit = n % 10
        m += digit
        n = n // 10
    return m


def main():

    print sum_of_digits(-123)
    print sum_of_digits(1325132435356)
    print sum_of_digits(6)
    print sum_of_digits(123)
    print sum_of_digits(-10)


if __name__ == '__main__':
    main()
