def is_int_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        print(n[::-1])
        return True
    return False


def main():
    is_int_palindrome(123)

if __name__ == '__main__':
    main()
