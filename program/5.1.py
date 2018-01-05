class TreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.bf = 0


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

def balancedTree(A):
    if A == None:
        depth = 0
        return True,depth

    lB , left = balancedTree(A.lchild)
    rB , right = balancedTree(A.rchild)
    if lB and rB:
        dif = left - right
        if dif <= 1 and dif >= -1:
            if left > right:
                depth = left +1
                return True,depth
            else:
                depth = right + 1
                return True,depth
    depth = 1
    return False,depth

A = [7,6,15,3,None,10,17,1,4,None,None,None,12,None,20]
B = [1,2,5,3,4,6,7]
s = BinTree(A)
t = BinTree(B)

Balance ,depth = balancedTree(s.root)
if Balance is True:
    print("the tree A is balance")
else:
    print("the tree A is not balance")
Balance ,depth = balancedTree(t.root)
if Balance is True:
    print("the tree B is balance")
else:
    print("the tree B is not balance")
