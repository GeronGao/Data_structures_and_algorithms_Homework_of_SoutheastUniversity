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

def maxSubTree(T,maxsum,subtree):

    if T==None:
        return 0,maxsum,subtree
    left ,maxsum,subtree = maxSubTree(T.lchild,maxsum,subtree)
    right ,maxsum,subtree = maxSubTree(T.rchild,maxsum,subtree)
    temp = T.data + left +right # 计算子树和
    if temp > maxsum: # 若子树和大于最大暂存值
        maxsum = temp #更新最大暂存值与对应节点
        subtree = T.data
    return temp,maxsum,subtree

subtree , maxsum = 0 , 0 # 设置两个全局变量 subtree 用于记录子树的节点
                        #maxsum用于记录最大值
A = [-4,-2,3,11,None,2,-5,-3,1,None,None,None,None,None,4]
t = BinTree(A)
t, x , y = maxSubTree(t.root,maxsum,subtree)
print("the sum-max subtree node is",y,", the max sum is",x)