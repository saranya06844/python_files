# Two Arrays
from itertools import count

fruits = ["apple", "banana", "cherry", "cherry"]
cars = ["Ford", "Volvo", "BMW"]

# Array methods

fruits.append("grape")
print("fruits: ", fruits)
# ----------------------------------------------------------------
Copy = fruits.copy()
print("copy of fruits: ", Copy)
# ----------------------------------------------------------------
fruits.clear()
print("after clearing fruits: ", fruits)
# ----------------------------------------------------------------
Count = fruits.count("cherry")
print("count of cherry: ", Count)
# ----------------------------------------------------------------
fruits.extend(cars)
print("after extending cars into fruits: ", fruits)
# ----------------------------------------------------------------
INdex_Cherry = fruits.index("Ford")
print("index of Ford: ", INdex_Cherry)
# ----------------------------------------------------------------
cars.insert(3, "toyoto")
print("cars after insert toyoto", cars)
# ----------------------------------------------------------------
cars.pop(1)
print("cars after pop 1:", cars)
# ----------------------------------------------------------------
cars.remove("Ford")
print("cars after remove ford: ", cars)
# ----------------------------------------------------------------
fruits.reverse()
print("fruits after reverse:", fruits)
# ----------------------------------------------------------------
fruits.sort()
print("fruits after sorting in alphabetic order: ", fruits)
