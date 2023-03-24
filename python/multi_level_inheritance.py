class First:
    def display_first(self):
        print("this is class first")

class Second(First):
    def display_second(self):
        print("this is class second")

class Third(Second):
    def display_third(self):
        print("this is class third")


x=Third()
x.display_first()