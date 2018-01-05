def majorityElement(A):
    mark = 0
    s = len(A)
    temp = A[1]
    for i in range(0, s, 1):# 第一个循环找出候选主元素
        if mark == -1:  # 当计数值小于0时，说明暂存值不是主元素
            mark = 0
            temp = A[i]

        if A[i] == temp:
            mark += 1
        else:
            mark -= 1
    mark = 0
    for i in range(0, s, 1):# 第二个循环验证所得主元素是否满足
                            # 排除 输出最后一个数的影响
        if A[i] == temp:
            mark += 1
    if mark >= s / 2:  # 当满足条件时，输出，当不满足输出-1
            return temp
    else:
        return -1



A = [3, 1, 2, 3, 3, 4, 3, 3, 5]
print("the majority element of A:",majorityElement(A))
B = [3, 1, 2, 3, 4, 5, 5]
print("the majority element of B:",majorityElement(B))