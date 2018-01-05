
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
def printList(L):#打印输出链表
    p = L
    while not p == None:
        print(p.data,end=' ')
        p = p.link
    print('end')
def inPlace(L):
    p = L #从前往后扫描的节点
    count = 0
    while not p == None:
        count = count + 1
        p = p.link
    p = L
    halfnumber = int(count / 2)
    for i in range(1,halfnumber+1,1):
        q = L  # 从后往前扫描的节点
        for j in range(1,count,1):
            q = q.link
        q.link = p.link#先将p后面的链接到q后面
        p.link = q# 再将q整个链接到p上
        for k in range(1,3,1):#P节点向后挪两个
            p = p.link
    p.link = None#最后给链表加一个none
    return L

B = [1,2,3,4,5,6,7,8,9,10,11,12]
print("list input:\n",B,"\nreplaced list:")
x= inPlace(createList(B))
printList(x)