def count_substrings(haystack, needle):
    count = 0
    for i in range(0, len(haystack)):
        if haystack[i] == needle[0]:
            for k in range(0, len(needle)):
                if haystack[i] != needle[k]:
                    break
                else:
                    i = i + 1
                if(k == len(needle) - 1):
                    count += 1
                if(i == len(haystack)):
                    return count
    return count


def main():
    print count_substrings("This is a test string", "is")
    print count_substrings("babababa", "baba")
    print count_substrings("This is this and that is this", "this")
    print count_substrings("Python is an awesome language to program with!", "o")
    print count_substrings("We have nothing in common!", "really?")

if __name__ == '__main__':
    main()
