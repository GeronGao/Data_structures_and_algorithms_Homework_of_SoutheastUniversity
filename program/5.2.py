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


def rTraverse(T,level):
    if T ==None:
        return
    if level ==1:# 到达要遍历的层后，显示
        print(T.data,end=" ")
        return
    rTraverse(T.rchild,level-1)
    rTraverse(T.lchild,level-1)
def lTraverse(T,level):
    if T ==None:
        return
    if level ==1:# 到达要遍历的层后，显示
        print(T.data,end=" ")
        return
    lTraverse(T.lchild,level-1)
    lTraverse(T.rchild,level-1)

A = [7,6,15,3,None,10,17,1,4,None,None,None,12,None,20]
t = BinTree(A)
print("the answer is:")
for i in range(1,5):
    if i%2 == 0 :
        rTraverse(t.root, i)#偶数层右遍历
    else:
        lTraverse(t.root, i)#奇数层左遍历