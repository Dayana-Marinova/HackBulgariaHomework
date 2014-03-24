import sys
from random import randint


def generate_numbers(filename, numbers):
    file = open(filename, "w")
    contents = []
    for i in range(0, int(numbers)):
        contents.append(str(randint(0, 1000)))

    file.write(", ".join(contents))
    file.close()


def main():
    generate_numbers(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
