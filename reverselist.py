import random
list1 = []
for i in range(100):
  list1.append(random.randint(1, 5))
list2 = []
for i in range(1, 6):
    list2.append(list1[i-1])
print(list2)