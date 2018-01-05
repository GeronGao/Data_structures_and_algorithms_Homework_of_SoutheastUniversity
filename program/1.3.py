def SelRange(InPut, OutPut, n, k, m):#输入数列，输出数列，输入的长度缓存 ，输出的长度缓存 ，输出的元素个数
    if (k == 0 and m !=0):
        print("{",end="")
        for j in range(0, m, 1):
            print(OutPut[j],end="")
            if j!=m-1:
                print(",",end="")#在元素之间输出逗号隔开
        print("}",end="")
    elif(k == 0 and m ==0):
        pass #排除空集的情况
    else:
        for i in range(n, k-1, -1):
            OutPut[m] = InPut[i-1]
            SelRange(InPut,OutPut, i - 1, k - 1, m + 1)


InPut = [1,4, 7, 8]
length = len(InPut)
OutPut =[0 for x in range(length)]#将输出的数列初始化为和输入数列一样的维数
for k in range (0,length+1,1):
    SelRange(InPut, OutPut, length, k, 0)
