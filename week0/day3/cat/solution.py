import sys


def cat(filename):
    file = open(filename, 'r')
    return file.read()


def main():
    if len(sys.argv) <= 1:
        return 'no argv given'
    for argv in range(1, len(sys.argv)):
        cat(sys.argv[argv])

if __name__ == '__main__':
    main()
