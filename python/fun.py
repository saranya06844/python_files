def hello():
    print("hello world")


# def hi(name):
#     print("my name is", name)
#
#
# hi("sara")
# hello()
# value = "saranya"
# hi(value)
#
# def Arbi_arguments(*value):
#     print(value[1])
#     print(value)
# Arbi_arguments("sara","john","arun","rudhra","sathya")

#global variable
value=10
def sample():
    #local variable

    value=45
    print(value)

sample()
print(value)
