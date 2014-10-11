def calculate_coins(sum):
    coins = [100, 50, 20, 10, 5, 2, 1]
    best_split = {1: 0, 2: 0, 100: 0, 5: 0, 10: 0, 50: 0, 20: 0}
    sum = int(sum * 100)
    for coin in coins:
        while sum - coin >= 0:
            best_split[coin] += 1
            sum -= coin
        if not sum:
            break
    return best_split
    
def main():
    print(calculate_coins(0.53))

if __name__ == '__main__':
    main()
