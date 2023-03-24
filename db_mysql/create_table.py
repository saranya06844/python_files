import pymysql
print("-------DATABASE CONNECTION--------")
x=pymysql.connect(host='localhost',user='root',
                  password='Saranyaj72160@',database='avodha')
cr=x.cursor()
a=input("enter a name of a customer")
b=input("enter a age of a customer")
cr.execute("insert into customer values(%s,%s)",(a,b))
x.commit()
chk="select * from customer where name=%s"

cr.execute(chk,a)
cur = cr.fetchall()
for i in cur:
    print(i)
x.close()
