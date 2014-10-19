def next_hack(n):
    while True:
        n += 1
        if bin(n)[:1:-1] == bin(n)[2::]:
            if bin(n).count('1') % 2 != 0:
                break
    return n


def main():
    print(next_hack(8031))

if __name__ == '__main__':
    main()
