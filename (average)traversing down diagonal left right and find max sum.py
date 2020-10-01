# Python 3 prorgam for finding max path in matrix 
# To calculate max path in matrix 

def findMaxPath(mat, n): 

    # To find max val in first row 
    res = -1
    for i in range(n): 
        res = max(res, mat[0][i]) 

    for i in range(1, n): 

        res = -1
        for j in range(n): 

            # When all paths are possible 
            if (j > 0 and j < n - 1): 
                mat[i][j] += max(mat[i - 1][j], 
                                max(mat[i - 1][j - 1], 
                                    mat[i - 1][j + 1])) 

            # When diagonal right is not possible 
            elif (j > 0): 
                mat[i][j] += max(mat[i - 1][j], 
                                mat[i - 1][j - 1]) 

            # When diagonal left is not possible 
            elif (j < n - 1): 
                mat[i][j] += max(mat[i - 1][j], 
                                mat[i - 1][j + 1]) 

            # Store max path sum 
            res = max(mat[i][j], res) 
    
    return res 

# Driver program to check findMaxPath 
for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    m=[]
    k=0
    for i in range(n)    :
        s=[]
        for j in range(n):
            s.append(l[k])
            k+=1
        m.append(s)
    
    
                    
    print(findMaxPath(m, n)) 

    # This code is contributed by Azkia Anam. 
# 
    # geeksforgeeks.org/maximum-path-sum-matrix/