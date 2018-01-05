class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
def createList( A):#创建链表
    n = len(A)
    first = None
    for i in range(n-1,-1,-1):
        t= Node(A[i])
        t.link = first
        first = t
    return first
def circleList(A,x):
    n = len(A)
    first = None
    for i in range(n-1, -1, -1):# 首先生成线性链表
        t = Node(A[i])
        t.link = first
        first = t
    circle = first
    temp = first
    i=0
    while circle.link is not None:
        if i == x:
            temp = circle # 记录环链入口
        circle = circle.link
        i+=1
    circle.link = temp # 将循环部分插入到线性链表最后，形成环链
    return first

def judgeCircleList(L):
    fast = L
    slow = L
    while True:
        fast = fast.link.link # 快速节点一次走两步
        slow = slow.link # 慢速节点一次走一步
        if fast == slow:  # 相遇表示是环链
            return True
        if fast is None or fast.link is None:
                            # 若找到了边界表示不是环链
            return False
def findCircleListEnt(L):
    fast = L
    slow = L # 定义两个节点
    while True :
        fast = fast.link.link # 快速节点一次走两步
        slow = slow.link # 慢速节点一次走一步
        if fast == slow:
            break
    temp1 = fast # 此时得到第一个相遇点
    temp2 = L # 第二个临时从头出发
    while not temp1 == temp2: #两个临时节点相遇即为环链入口
        temp1 = temp1.link
        temp2 = temp2.link
    return temp2.data


B = [0,9,5,0,6,1,7,2,8,3]
t = circleList(B,1)
p = createList(B)
#print('t is',judgeCircleList(t),', p is',judgeCircleList(p))

print("the entrance of circle is",findCircleListEnt(t))

