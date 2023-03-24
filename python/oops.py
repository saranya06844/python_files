class MysampleCalss:
    def hello(self, n,m):
        print("i",n,m)
    def Rec_var(self,n):
        self.name=n
    def print_var(self):
        print(self.name)

# create a object for class
x = MysampleCalss()
y=MysampleCalss()

# call a function in class by object
n="saranya"
x.hello(n,0)
x.Rec_var("saranya")
y.Rec_var("charru")
x.print_var()
y.print_var()
# or
MysampleCalss.hello(x,"sara",6)

#create a variable using object

