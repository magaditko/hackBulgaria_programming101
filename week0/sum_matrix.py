def sum_matrix(m):
    sum = 0
    for row in m:
        for column in row:
           sum += column
    return sum

def main():
    print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

if __name__ == '__main__':
    main()
