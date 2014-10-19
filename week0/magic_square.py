def list_sum(list):
    list_sum = 0
    for number in list:
        list_sum += number
    return list_sum


def find_sum_of_rows(matrix):
    rows = []
    for row in matrix:
        rows.append(list_sum(row))
    return rows


def find_sum_of_cols(matrix):
    cols = []
    mm = zip(*matrix)
    for row in mm:
        cols.append(list_sum(list(row)))
    return cols


def find_sum_of_diagonals(matrix):
    diagonals = []
    first_diagonal = [row[- i - 1] for i, row in enumerate(matrix)]
    second_diagonal = [row[i] for i, row in enumerate(matrix)]
    diagonals.append(list_sum(first_diagonal))
    diagonals.append(list_sum(second_diagonal))
    return diagonals


def magic_square(matrix):
    rows = find_sum_of_rows(matrix)
    cols = find_sum_of_cols(matrix)
    diagonals = find_sum_of_diagonals(matrix)

    sum_matrix = rows + cols + diagonals

    return sum_matrix[1:] == sum_matrix[:-1]

#print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
#print(find_sum_of_rows([[1,2,3],[4,5,6],[7,8,9]]))
#print(find_sum_of_cols([[1,2,3],[4,5,6],[7,8,9]]))
#print(find_sum_of_diagonals([[1,2,3],[4,5,6],[7,8,9]]))
