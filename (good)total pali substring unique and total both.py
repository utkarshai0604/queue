from collections import defaultdict
for _ in range(int(input())):
	n=int(input())
	s=input()
	m=defaultdict(int)
	# for odd pali
	ans=[]
	for i in range(n):
		for j in range(i+1):
			if(i+j>n-1):
				break
			if(s[i-j]==s[i+j]):
				if((i+j+1)-(i-j)>1):
					x=s[i-j:i+j+1]
					ans.append(x)
					m[s[i-j:i+j+1]]+=1
			else:
				break
	# for even pali
	
		for j in range(i+1):
			if(i+j+1>n-1):
				break
			if(s[i-j]==s[i+j+1]):
				if((i+j+2)-(i-j)>1):
					x=s[i-j:i+j+2]
					ans.append(x)
					m[s[i-j:i+j+2]]+=1
			else:
				break
	print("unique",(len(m)))
	print("total",len(ans))
	
