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

def getButton(s):#获得底部的数据
    temp = s.Pop()
    if s.isEmpty():
        return temp
    else:
        last = getButton(s)
        s.Push(temp)
        return last

def reverseStack(s):
    if s.isEmpty():
        return s
    i = getButton(s) # 用递归将底部的数据返回
    s = reverseStack(s)# 递归调用自身，不断交换
    s.Push(i)
    return s


G = [2,1,4,3,6,5,8,7,9,0]
print("before:",G)
print("after:",end=" ")
st = stack()
for i in range(len(G) - 1, -1, -1):
    st.Push(G[i])#压栈测试
p=reverseStack(st)
while not p.isEmpty():
    print(p.Pop(),end=" ,")