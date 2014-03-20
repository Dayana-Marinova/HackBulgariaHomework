import sys


def lines_count(filename):
    print 'lines'
    count = 1
    file = open(filename, "r")
    for line in file:
        count += 1
    file.close()
    return count


def words_count(filename):
    print 'words'
    count = 1
    file = open(filename, 'r')
    for line in file:
        for char in line:
            if char == ' ' or char == '\n':
                count += 1
    file.close()
    return count


def chars_count(filename):
    print 'chars'
    count = 0
    file = open(filename, 'r')
    for line in file:
        for char in line:
            count += 1
    return count


def main():
    if sys.argv[1] == 'chars':
        print chars_count(sys.argv[2])
    elif sys.argv[1] == 'words':
        print words_count(sys.argv[2])
    elif sys.argv[1] == 'lines':
        print lines_count(sys.argv[2])
    else:
        return "There is a problem!"

if __name__ == '__main__':
    main()
