from is_prime import is_prime


def prime_number_of_divisors(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1
    return divisors


def main():
    print is_prime(prime_number_of_divisors(7))
    print is_prime(prime_number_of_divisors(8))
    print is_prime(prime_number_of_divisors(9))

if __name__ == '__main__':
    main()