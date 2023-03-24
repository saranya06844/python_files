
n=8
arr=[['*']*n for x in range(n)]

f=0
l=n-1

value=1
for o in range(4):
    m=n/2
    fm=m
    lm=m
    for i in range(n):
        for j in range(n):
            if(i>=f and i<=l and (j==fm or j==lm)):
               arr[i][j]=value
        
        fm=fm-1
        lm=lm+1
    for i in range(8):
        for j in range(8):
            print(arr[i][j],end="")
        print()
    print("==========================================")
    f=f+1
    l=l-1
    value=value+1
for i in range(8):
    for j in range(8):
           print(arr[i][j],end="")
    print()
        
