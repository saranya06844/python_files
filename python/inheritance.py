class BaseClass:
    def __init__(self):
        print("baseclass init")

    def welcome(self):
        print("welcome to the base class")

    def set_name(self,name):
        self.name=name


class SubClass(BaseClass):
    def __init__(self):
        #BaseClass.__init__(self)
        super().__init__()
        print("it's subclass init")

    def welcome(self):
        #BaseClass.welcome(self)
        super().welcome()
        print("welcome to the subclass")

    def display_name(sel):
        print("name:",sel.name)

# x=BaseClass()
# y=SubClass()
# x.welcome()
# y.welcome()
# y.welcome()

y=SubClass()
y.set_name("saranya")
y.display_name()
y.welcome()

