n=8
f=0
l=n-1
arr = [[" "]*n for i in range(n)]
mf=n/2
ml=n/2
for k in range(4):
    for i in range(n):
        for j in range(5):
            if(i>=f and i<=l):
                if (j==mf or j==ml):
                    arr[i][j]=k
        mf=mf-1
        ml=ml+1
    f=f+1
    l=l-1

for i in range(8):
    for j in range(5):
        print(arr[i][j],end="")
    print()

