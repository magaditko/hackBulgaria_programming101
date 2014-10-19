def count_substrings(haystack, needle):
    return haystack.count(needle)


def main():
    print(count_substrings("This is a test string", "is"))

if __name__ == '__main__':
    main()
