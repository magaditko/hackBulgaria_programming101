def groupby(func, seq):
    result = {}
    for number in seq:
        if func(number) not in result.keys():
            result[func(number)] = [number]
        else:
            result[func(number)].append(number)
        print(result)


def main():
    groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7])
    groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])

if __name__ == '__main__':
    main()
