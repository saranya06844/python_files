class sample:
    def set_name(self, name,num):
        self.name = name
        self.num=num

    def __add__(self, second_obj):
        name=self.name+" "+second_obj.name
        return name
    def __mul__(self, other):
        result=self.num*other.num
        return result
first_name = sample()
second_name = sample()

first_name.set_name("saranya",90)
second_name.set_name("charru",20)


full_name=first_name+second_name
total=first_name*second_name
print(total)
print(full_name)

