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

def insert(st,v):
    if st.isEmpty() or v <= st.Top():
        st.Push(v)
        return st
    t= st.Pop()
    insert(st,v)
    st.Push(t)

    return st
def newRange(s):
    if s.isEmpty():
        return s
    else:
        v = s.Pop()
        s = newRange(s)
        s = insert(s,v)
    return s

def stackSort(A):
    st = stack()
    for i in range(len(A)-1,-1,-1):
        st.Push(A[i])
    return newRange(st)



def stackSort1(A):
    st = stack()
    emp = stack()
    for i in range(len(A)-1,-1,-1):
        st.Push(A[i])
    flag = len(A)-1
    while flag != 0:
        for i in range(0,flag,1):
            temp = st.Pop()
            if temp > st.Top(): #若暂存值大，则压入空指针
                emp.Push(st.Pop())
            else:
                emp.Push(temp) #若暂存值小，则更新暂存值
                temp = st.Pop()
            st.Push(temp)

        while not emp.isEmpty():# 送还给st
            st.Push(emp.Pop())
        flag -= 1
    return st




B = [4,6,8,7,5,3,2,9,0,1]
print("before changing:",B)
print("after changing:",end=" ")
q = stackSort(B)
while not q.isEmpty():
    print(q.Pop(),end=" ,")

print("")
print("before changing:",B)
print("after changing:",end=" ")
p=stackSort1(B)
while not p.isEmpty():
    print(p.Pop(),end=" ,")

