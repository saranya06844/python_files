limit = int(input("enter the number"))
size = (limit * 2) - 1
a = [[9] * size for k in range(size)]
front = 0
last = size - 1

while limit > 0:
    for i in range(front,last+1):
        for j in range(front,last+1):
            if i == front or i == last or j == front or j == last:
                a[i][j] = limit


    front = front + 1
    last = last - 1
    limit = limit -1





for i in range(size):
    for j in range(size):
        print(a[i][j], end=" ")
    print()


