for _ in range(int(input())):
    n,ar,m=int(input()),list(map(int,input().split())),int(input())
    dp=[0]*(m+1)
    dp[0]=1
    for i in range(n):
        for j in range(ar[i],m+1):
            dp[j]+=dp[j-ar[i]]
    print(dp[m]) 

    # The problem is typically asked as: If we want to make change for {\displaystyle N}{\displaystyle N} cents, and we have infinite supply of each of {\displaystyle S=\{S_{1},S_{2},\ldots ,S_{m}\}}{\displaystyle S=\{S_{1},S_{2},\ldots ,S_{m}\}} valued coins, how many ways can we make the change? (For simplicity's sake, the order does not matter.)

# It is more precisely defined as:

# Given an integer {\displaystyle N}{\displaystyle N} and a set of integers {\displaystyle S=\{S_{1},S_{2},\ldots ,S_{m}\}}{\displaystyle S=\{S_{1},S_{2},\ldots ,S_{m}\}}, how many ways can one express {\displaystyle N}{\displaystyle N} as a linear combination of {\displaystyle S=\{S_{1},S_{2},\ldots ,S_{m}\}}{\displaystyle S=\{S_{1},S_{2},\ldots ,S_{m}\}} with non-negative coefficients?

# Mathematically, how many solutions are there to {\displaystyle N=\sum _{k=1\ldots m}{x_{k}S_{k}}}{\displaystyle N=\sum _{k=1\ldots m}{x_{k}S_{k}}} where {\displaystyle x_{k}\geq 0,k\in \{1\ldots m\}}{\displaystyle x_{k}\geq 0,k\in \{1\ldots m\}}
# https://algorithmist.com/wiki/Coin_change#Dynamic_Programmin
# dp 7
#==============NOTE==============#
# n=x1*s1+x2*s2+x3*s3
# n<=sum    s1, s2, s3<= coins
# here solution for x1, x2, x3 is same as this problem solution