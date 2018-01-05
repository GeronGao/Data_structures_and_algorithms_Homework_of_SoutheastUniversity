def SelRange(InPut, OutPut, n, k, m):
    if (k == 0):
        for j in range(0, m, 1):
            print(OutPut[j],end="")
        print(" ",end="")
    else:
        for i in range(n, k-1, -1):
            OutPut[m] = InPut[i-1]
            SelRange(InPut,OutPut, i - 1, k - 1, m + 1)
InPut = [1, 2, 4, 7, 8]
length = len(InPut)
k = 3
OutPut =[0 for x in range(k)]
SelRange(InPut, OutPut,length, k, 0)

