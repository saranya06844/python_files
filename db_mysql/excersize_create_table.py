import pymysql

x = pymysql.connect(host="localhost",user="root",password="Saranyaj72160@",database="soften")
cur = x.cursor()



print("-------DATABASE MODEL-------")

a= input("time")
b = input("my mood")

cur.execute("insert into saranya values(%s,%s)",(a,b))
x.commit()

print("DISPLAY VALUES/n")

chk="select * from saranya where time=%s"

cur.execute(chk,a)

display=cur.fetchall()

for i in display:
    print(i)
x.close()
