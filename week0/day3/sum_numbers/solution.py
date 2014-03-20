import sys
from random import randint


def sum_numbers(filename, n):
    sum = 0
    file = open(filename, "w")
    contents = []
    for i in range(0, int(n)):
        contents.append(str(randint(0, 1000)))
        sum += int(contents[i])
    file.write(" ".join(contents))
    file.close()
    print sum


def main():
    sum_numbers(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
