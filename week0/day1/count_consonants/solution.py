def count_consonants(str):
    str = str.lower()
    count = 0
    lists = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    for i in str:
        if i in lists:
            count += 1
    return count
