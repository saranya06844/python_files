
num = int(input("enter the limit you want"))

arr = [[0] * num for k in range(num)]

front = 0

last = num-1

count = 1
for i in range(num):
    for j in range(num):
        arr [i][j]=count
        count = count +1

for i in range(num):
    for j in range(num):
        print(arr[i][j],end=" ")
    print()

while(front <= last):

    for i in range(front,last+1,1):
        print(arr [front][i],end=" ")

    for i in range(front+1,last+1,1):
       print(arr[i][last],end=" ")

    for i in range(last-1,front-1,-1):
        print(arr[last][i],end=" ")

    for i in range(last-1,front,-1):
        print(arr[i][front],end=" ")

    front = front+1
    last = last-1

