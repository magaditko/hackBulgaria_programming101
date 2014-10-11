def simplify_fraction(fraction):
    first = fraction[0]
    second = fraction[1]
    for number in range(first, 1, -1):
        if first % number == 0 and second % number == 0:
            first = first // number
            second = second // number
    return (first, second)


def main():
    print(simplify_fraction((63, 462)))

if __name__ == '__main__':
    main()
