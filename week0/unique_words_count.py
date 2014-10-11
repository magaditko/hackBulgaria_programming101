import count_words as cw
def unique_words_count(arr):
    result = cw.count_words(arr)
    keys = len(result)   
    return keys

def main():
    print(unique_words_count(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
    main()
