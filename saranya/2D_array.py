a=[[1,2,3,7],[1,2,3,5]]
print(a)
print(a[0][1])
for i in range(2):
    for j in range(4):
        print(a[i][j],end=" ")
    print()

print("==============================================================================")
r=2
c=4
b = [[],[]]
for i in range(2):
    for j in range(4):
        b[i].append(c)
        c+=1

print(b)
for i in range(2):
    for j in range(4):
        print(b[i][j],end=" ")
    print()
print("===================================================")
col =2
row = 3
array_example = [[1]*row,[1]*col] # jagged array
print(array_example)
arr =[[5]*col for i in range(row)]
print(arr)
print("========================================================")
brr=[[1]*col]
print(brr)
print("==================================================")
crr =[[] for i in range(row)]
print(crr)
drr = [[0]*col]*row
print(drr)
