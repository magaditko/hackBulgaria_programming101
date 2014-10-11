import contains_digit as cd


def contains_digits(number, digits):
    result = True
    for digit in digits:
        if not cd.contains_digit(number, str(digit)):
            return False
    return result


def main():
    print(contains_digits(66660, [6, 0]))

if __name__ == '__main__':
    main()
