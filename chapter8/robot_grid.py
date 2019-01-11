def robot_grid(r, c, offlimits):
    dp = [[[] for column in range(c)] for row in range(r)]
    dp[0][0] = [[(0,0)]]
    for coord in offlimits:
        dp[coord[0]][coord[1]] = None
    # prepopulate top row
    for j in range(1, c):
        if dp[0][j] is not None:
            if dp[0][j-1] is None:
                dp[0][j] = None
            else:
                dp[0][j] = [dp[0][j-1][0] + [(0,j)]]
    # prepopulate leftmsot column
    for i in range(1,r):
        if dp[i][0] is not None:
            if dp[i-1][0] is None:
                dp[i][0] = None
            else:
                dp[i][0] = [dp[i-1][0][0] + [(i,0)]]
    # populate rest
    for i in range(1, r):
        for j in range(1, c):
            if dp[i][j] is not None:
                paths = []
                if dp[i][j-1] is not None:
                    paths += dp[i][j-1]
                if dp[i-1][j] is not None:
                    paths += dp[i-1][j]
                dp[i][j] = [
                    path + [(i,j)]
                    for path in paths
                ]
    if dp[r-1][c-1] is not None:
        return dp[r-1][c-1][0]
    return None
    
print(robot_grid(3,3,[(1,0), (1,1), (2,2)]))