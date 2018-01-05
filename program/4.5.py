import copy
def maxSubMatrix(T):
    n = len(T)
    answer = -10000
    total = copy.copy(T )#使用一个辅助函数，用于存放和
    for i in range(0,n):
        for j in range(1,n):
            total[i][j] += total[i][j-1]#累加
    for i in range(0,n):
        for j in  range(i,n):#将矩阵切分为从i到j行的子矩阵
            subSum = 0
            for k in range(1,n):#列遍历，找最小的子矩阵
                if subSum <0:
                    subSum = 0
                    sx = k
                    sy = i
                subSum += total[k][j] - total[k][i-1]
                if answer <subSum:
                    answer = subSum
                    ex = k
                    ey = j
    return answer,sx,sy,ex,ey


# 测试算例
T = [[0,-2,-7,0],[9,2,-6,2],[-4,1,-4,1],[-1,8,0,-2]]
answer ,sx,sy,ex,ey =maxSubMatrix(T)
print("the max sum is",answer)
print("the submatrix is")
for i in range(sx,ex+1):#用循环打印子矩阵
    for j in range(sy,ey+1):
        print(T[i][j],end="  ")
    print(" ")
