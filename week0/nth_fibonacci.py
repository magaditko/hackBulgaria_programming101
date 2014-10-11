def nth_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


def main():
    print(nth_fibonacci(1))
    print(nth_fibonacci(2))
    print(nth_fibonacci(3))
    print(nth_fibonacci(10))

if __name__ == '__main__':
    main()
