def MinD(A,x,y):
    n = len(A)
    TempXLocal,TempYLocal,tempMinD=0,n,0
    minD = 1000
    if x == y:
        return 0
    for i in range(0,n-1):
        if A[i] ==x:
            TempXLocal = i
        if A[i] == y:
            TempYLocal = i
        if TempXLocal!=TempYLocal:
            tempMinD=abs(TempYLocal- TempXLocal)
            if tempMinD<minD:
                minD = tempMinD
    return  minD

A = [1,4,3,2,6,5,6,7,4,3,2,3,1,5,9,8,6,4,2,5]
x,y = 3,7
print(MinD(A,x,y))

