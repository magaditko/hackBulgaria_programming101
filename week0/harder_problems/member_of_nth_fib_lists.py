import fibonacci_lists as fl


def member_of_nth_fib_lists(listA, listB, needle):
    n = 1
    length = 0
    while length <= len(needle):
        length = len(fl.nth_fib_lists(listA, listB, n))
        if fl.nth_fib_lists(listA, listB, n) == needle:
            return True
        n += 1
    return False


def main():
    print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
    print(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
    print(member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
    print(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))

if __name__ == '__main__':
    main()
