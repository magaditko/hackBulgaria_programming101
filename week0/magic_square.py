def magic_square(matrix):
    sum_rows = []
    sum_cols = 0
    sum_diags = 0

    for row in matrix:
        for col in row:
            sum_rows.append(col)
        
    print(sum_rows)
            
magic_square([[1,2,3],[4,5,6],[7,8,9]])
