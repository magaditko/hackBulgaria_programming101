import sum_of_divisors as sod
def is_prime(n):
    divs = 1 + n
    if sod.sum_of_divisors(n) == divs:
        return True
    else:
        return False

def main():
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(-10))

if __name__ == '__main__':
    main()
