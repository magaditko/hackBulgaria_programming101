def nth_fib_lists(listA, listB, n):
    next = 3
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        while next <= n + 1:
            tmp = listA + listB
            listA = listB
            listB = tmp
            next += 1
        return listA


def main():
    print(nth_fib_lists([1, 2], [3, 4], 4))

if __name__ == '__main__':
    main()
