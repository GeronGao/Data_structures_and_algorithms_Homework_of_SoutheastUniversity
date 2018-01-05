class stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def Push(self, x):
        self.list.append(x)

    def Pop(self):
        if not self.isEmpty():
            return self.list.pop(len(self.list) - 1)
        else:
            return None

    def Top(self):
        if not self.isEmpty():
            return self.list[len(self.list) - 1]
        else:
            return None

def symmetry(A):
    temp = stack()
    for i in range(0,len(A)-1,1):
        if A[i] == A[i+1]:# 寻找相邻两个相同的字符串
            j = 0
            while A[i-j] == A[i + j + 1]:
                j += 1#当找到一个满足条件时，向两端搜索，计数值加一
                if i+j+1==len(A):
                    break
            temp.Push(j)#使用堆栈存计数值
        else:
            pass
    if temp.isEmpty():
        return None
    else:
        maxX = temp.Pop()
        while not temp.isEmpty():
            if temp.Top()>maxX:#找出计数值的最大值
                maxX = temp.Pop()
            else:
                temp.Pop()
    return maxX*2


A = 'abcdefg'
print("the number of longest symmetry char in A:",symmetry(A))
B= 'googleelgo'
print("the number of longest symmetry char in B:",symmetry(B))


