def calculate_coins(sum):
    sum = int(sum * 100)
    dictionary = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}
    list_of_coins = [100, 50, 20, 10, 5, 2, 1]
    while sum > 0:
        for coin in list_of_coins:
            if(coin <= sum):
                sum = sum - coin
                dictionary[coin] += 1
                break
    return dictionary


def main():
    print calculate_coins(0.53)
    print calculate_coins(1.56)
    print calculate_coins(10.73)

if __name__ == '__main__':
    main()
