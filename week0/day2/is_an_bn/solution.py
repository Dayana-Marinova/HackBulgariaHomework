def is_an_bn(word):
    length = len(word)
    if length % 2 != 0:
        return False
    for m in range(0, len(word)):
        if word[m] != 'a' and word[m] != 'b':
            return False
    else:
        rev = ""
        for i in word:
            rev = i + rev
        for k in range(0, len(word) / 2):
            for l in range(0, len(rev) / 2):
                if word[k] == rev[l]:
                    return False
        else:
            return True
