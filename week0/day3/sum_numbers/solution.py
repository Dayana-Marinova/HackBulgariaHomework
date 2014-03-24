import sys


def sum_numbers(filename):
    sum = 0
    file = open(filename, "r")
    content = file.read()
    countent_numbers = content.split(" ")
    for number in countent_numbers:
        number = int(number)
        sum += number
    return sum


def main():
    sum_numbers(sys.argv[1])

if __name__ == '__main__':
    main()
