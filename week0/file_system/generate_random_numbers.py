import sys
from random import randint


def main():
    file = open(sys.argv[1], 'w')
    for number in range(int(sys.argv[2])):
        random_number = randint(1, 1000)
        file.write(' '.join(str(random_number)))
    file.close()

if __name__ == '__main__':
    main()
