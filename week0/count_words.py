def count_words(arr):
    result = {}
    for item in arr:
        if item in result.keys():
            result[item] += 1
        else:
            result[item] = 1
    return result


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
    main()
