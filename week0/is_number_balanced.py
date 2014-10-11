def is_number_balanced(n):
    num = str(n)
    middle = len(num) // 2
    left_side_sum = 0
    right_side_sum = 0
    for digit in range(0, middle):
        left_side_sum += int(num[digit])
        right_side_sum += int(num[digit])
    if left_side_sum == right_side_sum:
        return True
    else:
        return False


def main():
    print(is_number_balanced(1238033))

if __name__ == '__main__':
    main()
