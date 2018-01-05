
def findMinCost(A):
    line = len(A)
    row = len(A[0])
    position = A
    for i in range(1,line):#第一列依次相加
        position[i][0] += position[i-1][0]
    for j in range(1,row):#第一行依次相加
        position[0][j] += position[0][j-1]
    for i in range(1,line):
        for j in range(1,row):# 每个元素都选择自己左边或者上边数据的较小值与自身相加
            position[i][j] += min(position[i-1][j],position[i][j-1])
    return position[line-1][row-1]#最后一位即为最小耗费


A = [[1,1,1,4],[4,3,1,3],[3,1,2,1],[1,1,4,1]]
print("the min cost is",findMinCost(A))
