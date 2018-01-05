def tracking(A):
    line = len(A)
    row = len(A[0])
    position = [[0 for i in range(row)] for j in range(line)]
    for i in range(line):
        position[i][0] = 1 # 左边界都为1
    for j in range(row):
        position[0][j] = 1 # 上边界都为1
    for i in range(1,line):
        for j in range(1,row):
            if A[i][j]==0: # 没有障碍物，则将左边和上边的量相加，表示有路径
                position[i][j] = position[i-1][j] + position[i][j-1]
            else:# 障碍物处 归零，表示没有路径
                position[i][j] = 0
    return position[line-1][row-1]


A = [[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0]]
print("the number of tracking is",tracking(A))
