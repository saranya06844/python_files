# num = int(input("enter a year"))
# if(num%4 == 0):
#     if(num %100== 0):
#         if(not(num % 400 == 0)):
#             print("is not leep year ")
#         else:
#             print("is a leap year")
#     else:
#         print("is a leap year")
# else:
#     print("is not a leap year")
# #100 2100
# # (a)+(b*c)
# #ab or ac
#
# if ((num%4 ==0) and (num%100 != 0 or num%400 ==0)):
#     print("is a leap year")
# else:
#     print("is not a leap year")

b = [3, 4, 3, 6, 6]
" for value in sequence:"
#
# list tuple  set
# for i in range(7):
#     print(i)
#
# for i in range(2, 7):
#     print(i)
#
# for i in range(2, 7, 2):
#     print(i)
# print("=============================================")
#
# for i in range(10, 2, -1):
#     print(i)

# list = [4, 3, 'sejl', 'dsdl']
# tuple = (3, 3, 5, 'gi', 'gd')
# set = {3, 6, 'd', 'd', 'd'}
# dictionary = {'id1': 5, 'id2': 'dadd'}
# string = "saranya"
c=4
r=4
array = [[2]*c for i in range(r)]
k=0            #r>i
for i in range(r):# I=0
    for j in range(c):# j=1
        array [i][j]=k
        k+=1# k=k+1

for i in range(r):
    for j in range(c):
        s=str(array[i][j])
        if len(s)==2:
            print(array[i][j],end="  ")
        else:
            print(array[i][j], end="   ")
    print()

# c colum
# r row
# 00 01 02
#10 11 12

for i in range(5):
    for j in range(i,5-1):# i
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
