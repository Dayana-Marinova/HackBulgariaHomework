import sys


def concat_files(file1, file2):
    fname = 'MEGATRON.txt'
    file_array = []
    file1_open = open(file1, 'r')
    file_array.append(file1_open.read())
    file1_open.close()
    file2_open = open(file2, 'r')
    file_array.append(file2_open.read())
    file2_open.close()
    file = open(fname, 'a')
    file.write("\n".join(file_array))
    file.close()
    file = open(fname, 'r')
    return file.read()


def main():
    concat_files(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
