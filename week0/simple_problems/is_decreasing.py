def is_decreasing(seq):
    result = True
    for number in range(len(seq) - 1):
        if seq[number] <= seq[number + 1]:
            result = False
    return result


def main():
    print(is_decreasing([5, 4, 3, 2, 1]))

if __name__ == '__main__':
    main()
