def prime_factorization(n):
    result = []
    divisors = []
    for number in range(2, n+1):
        while n % number == 0:
            divisors.append(number)
            n //= number
            #remove duplicates and sort
        sorted_divisors = sorted(list(set(divisors)))
        for value in sorted_divisors:
            result.append((value, divisors.count(value)))
        return result

def main():
    print(prime_factorization(10))

if __name__ == '__main__':
    main()
