import random
numbahlist = []
for i in range(1, 500):
    answer = random.randint(1, 100)
    numbahlist.append(answer)
for i in range(500):
    if numbahlist[i] == 42:
        print("I found the meaing of life!!")
        break
    else:
        print("I didn't find the meaning of life.")
        break