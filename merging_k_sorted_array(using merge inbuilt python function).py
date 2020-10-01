# merge function merge two arrays
# of different or same length
# if n=max(n1, n2)
# time complexity of merge is
#max(o(n log(n)))
from heapq import merge
#function for meging k arrays
def mergeK(arr, k):    
    l=arr[0]
    for i in range(k-1):
        l=list(merge(l, arr[i+1]))
    return l
# for printing array
def printArray(arr):
    print(*arr)


# driver code
arr=[[2, 6, 12 ], 
    [ 1, 9 ], 
    [23, 34, 90, 2000 ]]
k=3
l=mergeK(arr, k)
printArray(l)
# basic concept for sorting of k sorted array is
# 1. Create an output array.
# 2. Create a min heap of size k and insert 1st element in all the arrays into the heap
# 3. Repeat following steps while priority queue is not empty.
# …..a) Remove minimum element from heap (minimum is always at root) and store it in output array.
# …..b) Insert next element from the array from which the element is extracted. If the array doesn’t have any more elements, then do nothing.