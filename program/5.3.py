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



def pathCost(T,n,path,L): # T为树，n为路径代价对比值，
                            # path传递路径，L传递路径长度
    if T is not None:
        value = 0
        L += 1
        path[L] = T.data # 将路径都存在Path数列中
        for i in range(0,L+1):
            value += path[i] # 遍历计算路径代价
        if value == n: # 若路径代价满足要求 则输出节点
            print(T.data,end="  ")
        pathCost(T.lchild,n,path,L) # 递归调用
        pathCost(T.rchild,n,path,L)
        L -= 1

path = [0 for i in range(10)]
C = [10,5,12,7,None,None,4]
s = BinTree(C)
print("the nodes which cost 22 are ",end=" ")
pathCost(s.root,22,path,L=-1)