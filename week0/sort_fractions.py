def sort_fractions(fractions):
    values = []
    result = []
    for fraction in fractions:
        value = fraction[0] / fraction[1]
        values.append([value, fraction])
    values.sort()
    for item in values:
        result.append(item[1])
    print(result)


def main():
    sort_fractions([(2, 3), (1, 2), (1, 3)])

if __name__ == '__main__':
    main()
