class TreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.bf = 0

    def getData(self):return self.data
    def setData(self, item):self.data = item
    def getLeft(self):return self.lchild
    def getRight(self):return self.rchild
    def setLeft(self, L):self.lchild = L
    def setRight(self,R):self.rchild = R



class BinTree:
    def __init__(self, A):
        L = len(A)
        if L ==0:
            self.root = None
        else:
            if L > 0:
                B = [TreeNode(A) for i in range(len(A))]
                for i in range(L):
                    if A[i] != 0:
                        B[i] = TreeNode(A[i])
                for i in range(L):
                    if 2 * i + 1 < L and A[i] != None and A[2 * i + 1] != None:
                        B[i].lchild = B[2 * i + 1]
                    if 2 * i + 2 < L and A[i] != None and A[2 * i + 2] != None:
                        B[i].rchild = B[2 * i + 2]
                self.root = B[0]
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False


def wightedPathLen(T,L,answer):#L 用于传递路径长度 answer用于传递带权路径长度
                                #T传递树

    if T != None:
        if T.lchild == None and T.rchild == None:
            answer += L * T.data#当到达叶节点时,自加路径长度×权值
        L += 1
        L , answer = wightedPathLen(T.lchild,L,answer)
        L, answer = wightedPathLen(T.rchild,L,answer)
        L -= 1
    return L,answer


A = [7,6,15,3,None,10,17,1,4,None,None,None,12,None,20]
B = [1,2,5,3,4,6,7]
C = [10,5,12,7,None,None,4]
t = BinTree(C)

x,y = wightedPathLen(t.root,L = 0,answer = 0)
print("the length of path is",y)


