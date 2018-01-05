
def findTreeHigh(A):
    line = len(A)
    row = len(A[0])
    position = A
    for i in range(1,line):#第一列依次相加,对角线依次相加
        position[i][0] += position[i-1][0]
        position[i][i] += position[i-1][i-1]
    for i in range(2,line):
        for j in range(1,i):# 每个元素都选择自己左上或者上边数据的较大值与自身相加
            position[i][j] += max(position[i-1][j-1],position[i-1][j])
    return max(position[line-1])#最后列最大值即为最大路径，即为高度


A = [[17,0,0,0,0],[13,31,0,0,0],[11,20,15,0,0],[25,23,35,19,0],[14,22,37,18,14]]
print("the tree height is",findTreeHigh(A))