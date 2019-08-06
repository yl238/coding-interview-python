
def set_zeros(matrix):
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    
    for i in range(len(row)):
        if row[i]:
            nullify_row(matrix, i)
    
    for j in range(len(col)):
        if col[j]:
            nullify_col(matrix, j)
    return matrix
    

def nullify_row(mat_x, row):
    for j in range(len(mat_x[0])):
        mat_x[row][j] = 0

def nullify_col(mat_x, col):
    for i in range(len(mat_x)):
        mat_x[i][col] = 0


if __name__ == '__main__':
    mat = [[2, 1, 3, 3], [1, 0, 1, 1], [2, 1, 2, 0]]
    print(set_zeros(mat))