def sum_of_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n = n // 10
    print(sum)

sum_of_digits(1325132435356)
sum_of_digits(123)
sum_of_digits(6)
sum_of_digits(-10)
