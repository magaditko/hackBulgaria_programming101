import is_prime as ip


def goldbach(n):
    first = n // 2
    second = n // 2
    result = []
    while second <= n:
        if ip.is_prime(first) and ip.is_prime(second):
            result.append((first, second))
        first -= 1
        second += 1
    return result


def main():
    print(goldbach(100))

if __name__ == '__main__':
    main()
