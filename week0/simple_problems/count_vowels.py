from count_substrings import count_substrings


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    result = 0
    for character in vowels:
        result += count_substrings(str, character)
    return result


def main():
    print(count_vowels("Theistareykjarbunga"))

if __name__ == '__main__':
    main()
