import random


length = random.randint(3, 10)
lst1 = []
for i in range(length):
    lst1.append(random.randint(1, 10))
print(lst1)
lst2 = [lst1[0], lst1[2], lst1[-2]]
print(lst2)