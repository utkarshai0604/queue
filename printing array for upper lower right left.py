a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

n=len(a)
# printing right upper triangle diagonal included
print("")
print("printing right upper triangle diagonal included\n")
for i in range(0, n):
    for j in range(n-i):
        
        print(a[i][j],end=" \t")
    print("")

print("printing right upper triangle diagonal not included\n")
for i in range(0, n):
    for j in range(n-i-1):
        
        print(a[i][j],end=" \t")
    print("")

print("printing left lower triangle diagonal included\n")
for i in range(0, n):
    for j in range(i+1):
        
        print(a[i][j],end=" \t")
    print("")

print("printing left lower triangle diagonal not included\n")
for i in range(0, n):
    for j in range(i):
        
        print(a[i][j],end=" \t")
    print("")

print("printing right upper triangle diagonal included\n")
for i in range(0, n):
    for j in range(0, i):
        print(" ", end="\t")
    for j in range(i,n):
        
        print(a[i][j],end=" \t")
    print("")

print("printing right upper triangle diagonal not included\n")
for i in range(0, n):
    for j in range(0, i):
        print(" ", end="\t")
    for j in range(i+1,n):
        
        print(a[i][j],end=" \t")
    print("")


print("printing right upper triangle diagonal included\n")
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end="\t")
    for j in range(n-i-1, n):
      
        print(a[i][j],end=" \t")
    print("")

print("printing right upper triangle diagonal not included\n")
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end="\t")
    for j in range(n-i, n):
      
        print(a[i][j],end=" \t")
    print("")

# http://webservers.amtron.in/ccsu/webApp/dashboardStudent.php?lnk=prvwfsUG

