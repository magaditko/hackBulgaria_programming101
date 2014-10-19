import sys


def cat(filename):
    file = open(filename, "r")
    content = file.read()
    print(content)


def main():
    filename = sys.argv[1]
    cat(filename)

if __name__ == "__main__":
    main()
