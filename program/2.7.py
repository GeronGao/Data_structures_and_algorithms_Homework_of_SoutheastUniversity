def midNumber(A):
    cand = [0 for i in range (len(A))]
    idx = 1# 在cand数组上的指针
    maxN , cand[0]= A[0], A[0]
    for i in range(1, len(A) ,1):
        if A[i] >= maxN : # 满足后面数比前面大
            cand[idx] = A[i] # 将数更新至cand数组
            idx += 1 # 指针后移
            maxN = A[i]
        else:
            while idx > 0 and cand[idx - 1] > A[i]:
                idx -= 1# 指针前移删除前面数字比较大的部分
    for j in range(0, idx, 1):#输出中间值
        print(cand[j],end=" ")
# 函数调用测试
A = [3,1,6,4,5,7,9,8,10,14,12]
print("the middle mumber are",end=" ")
midNumber(A)