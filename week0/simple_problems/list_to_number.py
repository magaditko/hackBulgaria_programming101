def list_to_number(digits):
    result = ""
    for number in digits:
        result += str(number)
    return result


def main():
    print(list_to_number([1, 2, 3]))

if __name__ == '__main__':
    main()
