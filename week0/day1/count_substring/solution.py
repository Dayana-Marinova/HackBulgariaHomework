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
