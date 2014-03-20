def simplify_fraction(fraction):
    nominatior = fraction[0]
    denominator = fraction[1]
    if nominatior == 0:
        return "we can not divide by zero"
    if denominator == 0:
        return (0, 0)
    max_number = max(nominatior, denominator)
    for i in range(2, max_number):
        if nominatior % i == 0 and denominator % i == 0:
            nominatior /= i
            denominator /= i
            return simplify_fraction((nominatior, denominator))
    return (nominatior, denominator)


def main():
    print simplify_fraction((3, 9))
    print simplify_fraction((1, 7))
    print simplify_fraction((4, 10))
    print simplify_fraction((63, 462))
    print simplify_fraction((8, 12))

if __name__ == '__main__':
    main()
