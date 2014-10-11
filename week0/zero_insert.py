def zero_insert(n):
    number = str(n)
    digit = len(number) - 1
    while digit > 0:
        if number[digit] == number[digit - 1]:
            number = number[:digit] + "0" + number[digit:]
        elif (int(number[digit]) + int(number[digit - 1])) % 10 == 0:
            number = number[:digit] + "0" + number[digit:]
        digit -= 1
    return int(number)

def main():
    print(zero_insert(116457))

if __name__ == '__main__':
    main()
