import sys


def main():
    file = open(sys.argv[1], 'r')
    content = file.read()
    numbers = content.split(' ')
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += int(number)
    print(sum_of_numbers)

if __name__ == '__main__':
    main()
