def count_vowels(str):
    str = str.lower()
    count = 0
    for i in str:
        if i == 'a' or i == 'e' or i == 'o' or i == 'y' or i == 'i' or i == 'u':
            count += 1
    return count


def main():
    print count_vowels("Dayana")
    print count_vowels("I love you!")
    print count_vowels("neprotivokonstitucionstvovatelstvuvaite")

if __name__ == '__main__':
    main()
