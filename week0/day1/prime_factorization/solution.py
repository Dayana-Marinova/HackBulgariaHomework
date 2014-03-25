def prime_factorization(n):
    dictionary = {}
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                dictionary[i] = 0
                while n % i == 0:
                    n /= i
                    dictionary[i] += 1
    return dictionary
