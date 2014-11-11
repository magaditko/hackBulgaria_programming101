from magic_square import list_sum, find_sum_of_rows, find_sum_of_cols

STEP = 3
COLUMNS = 3
ROWS = 9


def split(list):
    list = [list[i: i + STEP] for i in range(0, len(list), STEP)]
    return list


def split_rows(matrix):
    rows = []
    for row in enumerate(matrix):
        rows.append(split(matrix[row[0]]))
    return row


def find_little_squares(matrix):
    matrix = split_rows(matrix)
    list_squares = []
    for col in range(COLUMNS):
        for row in range(ROWS):
            list_squares.append(matrix[row][col])
    list_squares = split(list_squares)
    return list_squares


def find_sum_of_squares(matrix):
    squares_sum = []
    squares = find_little_squares(matrix)

    for square in squares:
        square_sum = 0
        for row in list:
            square_sum += list_sum(row)
        squares_sum.append(square_sum)
    return squares_sum


def is

def sudoku_solved(matrix):
    rows_sum = find_sum_of_rows(matrix)
    cols_sum = find_sum_of_cols(matrix)
    squares_sum = find_sum_of_squares(matrix)

    if rows_sum == cols_sum == squares_sum:
        return True
    else:
        return False
