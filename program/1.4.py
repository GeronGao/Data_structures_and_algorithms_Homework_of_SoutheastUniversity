def MaxDiff(A):
    n = len(A)
    AMaxTemp=A[0]
    DmaxTemp=A[0]
    dmax = 0
    for i in range(1,n):
        if A[i-1] > AMaxTemp:
            AMaxTemp = A[i-1]
        DmaxTemp = AMaxTemp - A[i]#前面的数减去后面的数的最大值
        if DmaxTemp > dmax:
            dmax = DmaxTemp
    return dmax

A = [0,3,4,24,5,1,16,7]
print(MaxDiff(A))
