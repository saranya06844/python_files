n=int(input("enter the limit"))
n=n+1
for i in range(1,n):

    for j in range(i,n-1):
        print(" ", end=" ")

    for j in range(2*i-1):
        print("* ", end="")
    print()
n1=n-1
for i in range(1,n1):

    for j in range(i):
        print(" ",end=" ")
    for j in range(i-1,2*(n1-1)-i):
        print("* ",end="")
    print()

row = n+1
col = n+n-1
arr = [[0]*col for i in range(row)]

for i in range(row):
    for j in range(col):
        print(arr[i][j],end=" ")
    print()



