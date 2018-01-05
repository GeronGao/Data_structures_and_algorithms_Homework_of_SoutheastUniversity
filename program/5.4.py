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

def maxDiameter(T,maxD):
    if T == None:
        return 0,maxD
    left,maxD = maxDiameter(T.lchild,maxD)
    right,maxD = maxDiameter(T.rchild,maxD)
    if left +right > maxD:
        maxD = left +right
    if left >right:
        return left + 1,maxD
    else:
        return right + 1,maxD




A = [7,6,15,3,None,10,17,1,4,None,None,None,12,None,20]
B = [1,2,5,3,4,6]

s = BinTree(A)
t = BinTree(B)
x , sMax = maxDiameter(s.root,maxD = 0)
x , tMax = maxDiameter(t.root,maxD = 0)
print("the max diameter of A is",sMax)
print("the max diameter of B is",tMax)