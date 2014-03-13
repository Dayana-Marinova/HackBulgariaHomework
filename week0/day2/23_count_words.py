def count_words(arr):
    new_dic = {}
    count = 1
    for i in arr:
        if i in new_dic:
            new_dic[i] += 1
        else:
            new_dic[i] = count
    return new_dic


def main():
    print count_words(['python', 'python', 'python'])
    print count_words(["apple", "banana", "apple", "pie"])

if __name__ == '__main__':
    main()
