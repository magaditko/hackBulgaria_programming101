def nth_fib_lists(first_list, second_list, n):
    if n == 1:
        return first_list
    elif n == 2:
        return second_list
    else:
        first_element = nth_fib_lists(first_list, second_list, n - 1)
        second_element = nth_fib_lists(first_list, second_list, n - 2)
        return first_element + second_element
