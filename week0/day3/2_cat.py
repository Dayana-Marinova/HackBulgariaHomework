import sys


def cat(filename):
    if (sys.argv) > 1:
        file = open(filename, 'r')
        print file.read()
    else:
        print 'no argv given'


def main():
    for argv in range(1, len(sys.argv)):
        cat(sys.argv[argv])

if __name__ == '__main__':
    main()
