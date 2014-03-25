def count_vowels(str):
    str = str.lower()
    count = 0
    for i in str:
        if i == 'a' or i == 'e' or i == 'o' or i == 'y' or i == 'i' or i == 'u':
            count += 1
    return count
