import sys


def lines_count(filename):
    count = 0
    file = open(filename, "r")
    for line in file:
        count += 1
    file.close()
    return count


def words_count(filename):
    count = 0
    file = open(filename, 'r')
    for line in file:
        for char in line:
            if char == ' ' or char == '\n':
                count += 1
    file.close()
    return count


def chars_count(filename):
    count = 0
    file = open(filename, 'r')
    for line in file:
        for char in line:
            count += 1
    return count


def main():
    if sys.argv[1] == 'chars':
        chars_count(sys.argv[2])
    elif sys.argv[1] == 'words':
        words_count(sys.argv[2])
    elif sys.argv[1] == 'lines':
        lines_count(sys.argv[2])
    else:
        return "There is a problem!"

if __name__ == '__main__':
    main()
