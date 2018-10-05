import sys

def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0 or len(matrix) != len(matrix[0]):
        return False
    N = len(matrix)
    for layer in range(0, N/2):
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last-offset][first]
            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
    return True

if __name__ == "__main__":
    matrix = [[1,0,1],[0,1,0],[1,2,3]]
    rotate_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j])
