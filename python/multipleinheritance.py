class first:
    # def display_First(self):
    #     print("first")

    def commen(self):
        print("first common")

class second:
    # def display_Second(self):
    #     print("second")

    def commen(self):
        print("second common")

class third(first,second):
    def dispaly_Third(self):
        print("third")
    # def commen(self):
    #     print("third common")

x=third()

# x.display_First()
# x.display_Second()
# x.dispaly_Third()
print("---------------------------")
x.commen()
#the below code for know the order of the execution of function
print(third.mro())# mro - Method Resolution Order
