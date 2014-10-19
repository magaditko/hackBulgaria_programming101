import magic_square as ms


def split(list):
    list = [list[i: i + 3] for i in range(0, len(list), 3)]
    return list


def split_rows(matrix):
    tmp = []
    for i in enumerate(matrix):
        tmp.append(split(matrix[i[0]]))

    return tmp


def find_little_squares(matrix):
    matrix = split_rows(matrix)
    tmp = []
    for col in range(3):
        for row in range(9):
            tmp.append(matrix[row][col])
    tmp = split(tmp)
    return tmp


def find_sum_of_squares(matrix):
    squares_sum = []
    tmp = find_little_squares(matrix)

    for list in tmp:
        tmp_sum = 0
        for row in list:
            tmp_sum += ms.list_sum(row)
        squares_sum.append(tmp_sum)
    return squares_sum


def sudoku_solved(matrix):
    rows = ms.find_sum_of_rows(matrix)
    cols = ms.find_sum_of_cols(matrix)
    squares = find_sum_of_squares(matrix)

    if rows == cols == squares:
        return True
    else:
        return False
