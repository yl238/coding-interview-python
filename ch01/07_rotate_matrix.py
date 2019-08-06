import unittest

def rotate(matrix):
    if ((len(matrix)== 0) or (len(matrix) != len(matrix[0]))):
        return False
    n = len(matrix)
    for layer in range((n+1)//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]

            matrix[last-offset][first] = matrix[last][last-offset]

            matrix[last][last - offset] = matrix[i][last]

            matrix[i][last] = top
    return matrix

if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4]]
    
    mat2 = [[2, 4], [1, 3]]
    print(rotate(mat1))
    