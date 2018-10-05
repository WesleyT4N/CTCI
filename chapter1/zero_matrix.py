def zeroRow(m, rowNum):
    for i in range(len(m[0])):
        m[rowNum][i] = 0

def zeroColumn(m, colNum):
    for i in range(len(m)):
        m[i][colNum] = 0
    
def zeroMatrix(m):
    if m is None or len(m) == 0 or len(m[0]) == 0:
        return False
    M = len(m)
    N = len(m[0])
    row = [False] * M
    column = [False] * N
    for i in range(M):
        for j in range(N):
            if m[i][j] == 0:
                row[i] = True
                column[j] = True
    
    for i in range(len(row)):
        if row[i]:
            zeroRow(m, i)
    
    for j in range(len(column)):
        if column[j]:
            zeroColumn(m, j)
    return True

def zeroMatrix2(m):
    first_row_zero = False
    first_col_zero = False

    for i in range(len(m[0])):
        if m[0][i] == 0:
            first_row_zero = True
            break
    for j in range(len(m)):
        if m[j][0] == 0:
            first_col_zero = True
            break

    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0
    
    for i in range(1, len(m)):
        if m[i][0] == 0:
            zeroRow(m, i)
    for j in range(1, len(m[0])):
        if m[0][j] == 0:
            zeroColumn(m, j)
    if first_row_zero:
        zeroRow(m, 0)
    if first_col_zero:
        zeroColumn(m, 0)


if __name__ == "__main__":
    m = [[0, 1, 0], [1, 1, 1], [0, 1, 1]]
    zeroMatrix2(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j])