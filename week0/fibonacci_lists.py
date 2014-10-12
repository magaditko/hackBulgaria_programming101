def nth_fib_lists(listA, listB, n):
    tmp = listA
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        for i in range(n - 2):
            tmp.extend(listB)
            listA = listB
            listB = tmp
        return listB


def main():
    print(nth_fib_lists([], [], 100))

if __name__ == '__main__':
    main()
