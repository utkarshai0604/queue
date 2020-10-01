

from collections import Counter
def chkOutOfBound(i, j, m):
	f= (i<len(m) and j<len(m[0]) and i>0 and j>0)
	return 1


def func(m):
	if(not m):
		return 1
	else:
		return 0
arr, c1, c2, a1, a2= [], [], [], [], []
chk, trackR, trackC, r, c = 0, -1, 1, 8, 0

c_c = 0
c_a = 0
for i in range(9):
	arr.append(input())
#print(m[8-1][3])
while(chk<2):
	f=func(arr)
	print(str(c)+" "+str(8-r))
	r += trackR
	c += trackC
	if(arr[r][c]=="*"):
		f=chkOutOfBound(r,c,arr)
		if(f):
			ki=arr[0][0]
		
	

		chk += 1
	if r==0 or r==8:
		trackR = -trackR
	elif c==0 or c==19:
		trackC = -trackC
		
	elif arr[r][c]=="c":
		f=chkOutOfBound(r,c,arr)
		if(f):
			ki=arr[0][0]
		c1.append(10*c+r)
		if trackR==trackC:
			trackC = -trackC
		else:
			trackR = -trackR
	elif arr[r][c]=="a":
		f=chkOutOfBound(r,c,arr)
		if(f):
			ki=arr[0][0]
		#print("sdf")
		a1.append(10*c+r)
		if trackR==trackC:
			#print("dfsdg")
			trackR = -trackR
		else:
			trackC = -trackC
print(str(c)+' '+str(8-r))
for r in range(9):
	temp = Counter(arr[r])
	#print(temp)
	c_c += temp['c']
	c_a += temp['a']
	for c in range(20):
		if(10*c+r in a1 or 10*c+r in c1):
			f=chkOutOfBound(r,c,arr)
			if(f):
				ki=arr[0][0]
			print('-',end='')
		else:
			
			print(arr[r][c],end='')
	print()
print("safe="+str(c_c+c_a-len(a1)-len(c1)))
print("infected="+str(len(a1)+len(c1)))