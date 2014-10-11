def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    count = 0
    for character in str:
        if character in consonants:
            count += 1
    return count

def main():
    print(count_consonants("grrrrgh!"))

if __name__ == '__main__':
    main()
