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

def judgeLine(A,B):
    s = stack()
    stComp = stack()
    for i in range(len(A)-1,-1,-1):
        stComp.Push(A[i])# 先将要比较的数存入堆栈
    j , k = 0 , 0
    while True:
        if (s.Top()==stComp.Top()):#比较两个堆栈顶
            stComp.Pop()#当相等时，弹栈，计数值加一
            s.Pop()
            k += 1
        else:
            if j!= len(B):# 当两个堆栈顶不相等时
                s.Push(B[j]) #B压栈
                j = j + 1

        if stComp.isEmpty() and k == len(B):
            print("true") #当比较的栈已经空，并且数组已经到头，满足条件
            return
        elif stComp.isEmpty() and s.Top()!=stComp.Top():
            print("false")
            return
        elif j>= len(B) and s.Top()!=stComp.Top():
            print("false")
            return
        else:
            continue


A = [0,1,2,3,4,5,6,7,8,9]
B = [4,6,8,7,5,3,2,9,0,1]
C = [4,3,2,1,0,9,8,7,6,5]
D = [2,5,6,7,4,8,9,3,1,0]
E = [1,2,3,4,5,6,9,8,7,0]
F = [1,4,7,9,8,6,5,3,0,2]
G = [2,1,4,3,6,5,8,7,9,0]
print("the result of B is",end=" ")
judgeLine(B,A)
print("the result of C is",end=" ")
judgeLine(C,A)


