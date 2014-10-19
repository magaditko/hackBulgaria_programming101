import sys


def main():
    final_file = open(sys.argv[-1], 'a')
    for arg in range(1, len(sys.argv) - 1):
        files = open(sys.argv[arg], 'r')
        content = files.read()
        final_file.write(''.join(content))
        files.close()
    final_file.close()

if __name__ == '__main__':
    main()
