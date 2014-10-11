def biggest_difference(arr):
    result = min(arr) - max(arr)
    return result

def main():
    print(biggest_difference([-10, -9, -1]))

if __name__ == '__main__':
    main()
