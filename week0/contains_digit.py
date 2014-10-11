def contains_digit(number, digit):
    if str(number).count(str(digit)) > 0:
        return True
    else:
        return False


def main():
    print(contains_digit(1234, 4))

if __name__ == '__main__':
    main()
