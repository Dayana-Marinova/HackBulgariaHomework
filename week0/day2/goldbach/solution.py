from is_prime import is_prime


def goldbach(n):
    prime_numbers = []
    rev_prime_numbers = []
    list_of_result = []
    result = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
    i = len(prime_numbers)
    while i > 0:
        i -= 1
        rev_prime_numbers.append(prime_numbers[i])
    for num in prime_numbers:
        for nums in rev_prime_numbers:
            if num + nums == n:
                list_of_result.append((num, nums))
    if len(list_of_result) == 1:
        return list_of_result
    elif len(list_of_result) == 2:
        if max(list_of_result[0]) != max(list_of_result[1]):
            print 'ok'
            return list_of_result
        else:
            list_of_result.remove(list_of_result[1])
            return list_of_result
    else:
        if len(list_of_result) % 2 == 0:
            for num in range(0, len(list_of_result) / 2):
                result.append(list_of_result[num])
            return result
        else:
            for num in range(0, len(list_of_result) / 2 + 1):
                result.append(list_of_result[num])
            return result


def main():
    print goldbach(100)
    print goldbach(10)
    print goldbach(4)
    print goldbach(8)

if __name__ == '__main__':
    main()
