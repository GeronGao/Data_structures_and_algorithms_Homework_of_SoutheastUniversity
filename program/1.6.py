def MaxSubsequenceSum(A):
    n = len(A)
    maxSum = 0
    tempSum = 0
    for i in range(0,n):
        tempSum = tempSum+A[i]
        if tempSum <0:
            tempSum =0
        if maxSum<tempSum:
            maxSum = tempSum
    return maxSum

A = [-2, 11, -4, 13, -5, -2 ]
print(MaxSubsequenceSum(A))