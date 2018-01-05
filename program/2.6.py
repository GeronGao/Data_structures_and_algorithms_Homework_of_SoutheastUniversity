def tMajorityElement(A):
    mark = 0
    s = len(A)
    temp = A[1]
    temp1 = A[1]
    for i in range(0, s, 1):# 第一个循环找出候选三分主元素
        if mark == -1:  # 当计数值小于0时，说明暂存值不是主元素
            mark = 0
            temp = A[i]

        if A[i] == temp:
            mark += 3
        else:
            mark -= 2
    mark = 0
    for i in range(0,s,1):
        if A[i] == temp: # 排除第一个候选三分主元素的影响
            continue
        else: # 在排除第一个候选三分主元素的影响后，剩下元素中存在主元素，作为第二个候选
            if mark == -1:  # 当计数值小于0时，说明暂存值不是主元素
                mark = 0
                temp1 = A[i]
            if A[i] == temp1:
                mark += 1
            else:
                mark -= 1
    mark = 0
    mark1 = 0
    for i in range(0, s, 1):# 第二个循环验证所得三分主元素候选是否满足
                            # 排除 输出最后一个数的影响
        if A[i] == temp:
            mark += 1
        if A[i] == temp1:
            mark1 += 1
    if mark > s / 3 and mark1 > s/3:  # 当满足条件时，输出，当不满足输出-1
        return temp ,temp1
    elif mark > s / 3 and not mark1 > s/3:
        return temp
    else:
        return -1



A = [3, 3, 3, 3, 4, 4, 4, 4, 5]
print("the answer of A is",tMajorityElement(A))
B = [4, 1, 2, 4, 4, 5, 5]
print("the answer of B is",tMajorityElement(B))
C = [1, 2, 3, 4, 5, 6, 7]
print("the answer of C is",tMajorityElement(C))