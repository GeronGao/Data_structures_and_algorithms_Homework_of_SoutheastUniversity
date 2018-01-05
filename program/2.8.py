def minDistance(A, B, C):
    i ,j ,k = 0 ,0 ,0
    minDis = abs(A[i]-B[j])+abs(A[i]-C[k])+abs(B[j]-C[k])

    while i < len(A) and j < len(B) and k < len(C):
        dis = abs(A[i]-B[j])+abs(A[i]-C[k])+abs(B[j]-C[k])
        if dis < minDis:
            minDis = dis
            X , Y , Z= A[i] , B[j] , C[k]
        # 找三个数组中尽量靠近的数
        if A[i] <= B[j] and A[i] <= C[k]:
            i += 1
        elif B[j] <= A[i] and B[j] <= C[k]:
            j += 1
        else:
            k += 1
    print("the min distance of A&B&C is",minDis)
    print("the position is",X,Y,Z)

# 测试实例
A = [5, 6, 7, 10]
B = [13, 14, 15, 17]
C = [16, 22, 24, 29, 32, 42]
minDistance(A, B, C)