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
