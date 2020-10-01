# Python program to count 
# number of subarrays 
# whose maximum element 
# is greater than K. 

# Return number of 
# subarrays whose maximum 
# element is less than or equal to K. 
def countSubarray(arr, n, k): 

	# To store count of 
	# subarrays with all 
	# elements less than 
	# or equal to k. 
	s = 0

	# Traversing the array. 
	i = 0
	while (i < n): 
	
		# If element is greater 
		# than k, ignore. 
		if (arr[i] > k): 
		
			i = i + 1
			continue
		
		# Counting the subarray 
		# length whose 
		# each element is less 
		# than equal to k. 
		count = 0
		while (i < n and arr[i] <= k): 
		
			i = i + 1
			count = count + 1
		

		# Suming number of subarray whose 
		# maximum element is less 
		# than equal to k. 
		s = s + ((count*(count + 1))//2) 
	

	return (n*(n + 1)//2 - s) 
	
# Driver code 
for _ in range(int(input())):
	n,k=input().split()
	n=int(n)
	k=int(k)
	l=list(map(int, input().split()))

	print(countSubarray(l, n, k)) 


# https://www.geeksforgeeks.org/count-subarrays-whose-maximum-element-greater-k/
# This code is contributed 
# by Anant Agarwal. 
