def countPS( str):

    n = len(str)
    cps=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n):
        cps[i][i]=1
    for L in range(2, n+1)    :
        for i in range(n-L+1):
            k=i+L-1
            if(str[i]==str[k]):
                cps[i][k]=cps[i+1][k]+cps[i][k-1]+1
            else:
                cps[i][k]=cps[i+1][k]+cps[i][k-1]-cps[i+1][k-1]
    return cps[0][n-1]
    


str1=input()
n=countPS(str1)
print(n)

# link:
# https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1x
# ques:
# Given a string str, your task is to complete the function countPs which takes a string str as its only argument and returns an integer denoting the no of palindromic subsequence (need not necessarily be distinct) which could be formed from the string str.

# Input:
# The first line of input contains an integer T, denoting the no of test cases then T test cases follow. Each test case contains a string str.

# Output:
# For each test case output will be an integer denoting the no of palindromic subsequence which could be formed from the string str.

# Constraints:
# 1<=T<=100
# 1<=length of string str <=30

# Example(To be used only for expected output):
# Input:
# 2
# abcd
# aab

# Output:
# 4
# 4

# Explanation:
# For the first test case
# palindromic subsequence are : "a" ,"b", "c" ,"d"

# For second test case
# palindromic subsequence are :"a", "a", "b", "aa"
