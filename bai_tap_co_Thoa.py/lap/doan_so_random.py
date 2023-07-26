import random

x = random.randint(1,30)
print(x)

for i in range(4):
    n = int(input())

    if n == x:
        print("đoán đúng rồi bro! Ok đấy")
        break
    else:
        if n > x:
            print("so doan > so random")
        else:
            print("so doan < so random")