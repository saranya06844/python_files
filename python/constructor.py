# It's a constructor
class MyClass:

    year=2022   # Class variable
    def __init__(self,name,age,place): # It's a constructor
       # print (name,age,place)
        self.name=name #we assign a value in according to object
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place
    def display(self):
        print("year:",MyClass.year)
        print("name:",self.name)
        print("age:",self.age)
        print("place",self.place)

    @classmethod
    def add_class(cls):
        cls.year=cls.year+1

    @staticmethod
    def static_display():
        print("welcome")

MyClass.static_display()

x = MyClass("sarany",22,"kottayam")
y = MyClass("Deuv",22,"alappuzha")


x.display()
y.display()

print("-------------------------------------------------")
x.add_age()
y.add_age()

MyClass.year=MyClass.year+1

x.display()
y.display()

print("-------------------------------------------------")
x.add_age()
y.add_age()

x.relocate("chennai")
y.relocate("kochi")

MyClass.add_class()

x.display()
y.display()



