def is_increasing(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True


def main():
    print is_increasing([1, 2, 3, 4, -10])
    print is_increasing([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print is_increasing([9, 8, 7, 6, 5, 4])
    print is_increasing([1, 1, 1, 1, 1, 1])

if __name__ == '__main__':
    main()
