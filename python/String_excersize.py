# how to declare a string

a = "saranay"  # also use '___'
"sara"
Multi_line_String = '''Nothing is impossible
 everything is possible'''  # also use""" __"""
print(a, "\n", Multi_line_String)

print("_____________________________________________________")

# String as Array or accessing characters in String
eg1 = "hello world"  # h as in 0 th position
print(eg1[1:4])  # it starts from e(1st) and end on l(3rd position)
print("_____________________________________________________")

# looping through a string
for x in eg1:  # take a string variable
    print(x)
for i in "saranya":  # take a string directly
    print(i)
print("_____________________________________________________")

# To find length
eg2 = "saranya"
length = len(eg2)
print(length)  # or
print(len(eg2))

print("_____________________________________________________")

# check String(in)

eg3 = "I can do this"
print("do" in eg3)# output is 'True'

# or use if statement(in)
if "do" in eg3:
    print("yes, 'do' is present")

# check if not(not in)

eg4 = "I can do this"
print("eye" not in eg4)# output is 'True'

# or in if(not in)
if "eye" not in eg4:
    print("yes, the element not present")

print("_____________________________________________________")
