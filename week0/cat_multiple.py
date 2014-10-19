import sys


def main():
    for arg in range(1, len(sys.argv)):
        file = open(sys.argv[arg], 'r')
        content = file.read()
        print(content)
        file.close()

if __name__ == '__main__':
    main()
