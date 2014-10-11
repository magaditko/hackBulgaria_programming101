def sevens_in_a_row(arr, n):
    result = False
    for i in range(len(arr) - n):
        if arr[i] == 7:
            result = True
            for j in range(i + 1, i + n):
                if arr[j] != 7:
                    result = False
                if result:
                    break
    return result


def main():
    print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))

if __name__ == '__main__':
    main()
