import is_prime as ip


def prime_number_of_divisors(n):
    count_divisors = 0
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            count_divisors += 1
        divisor += 1
    if ip.is_prime(count_divisors):
        return True
    else:
        return False


def main():
    print(prime_number_of_divisors(8))

if __name__ == '__main__':
    main()
