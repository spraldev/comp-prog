import random


def verify(x, y):
    return x + y > x^y and x + (x^y) > y and y + (x^y) > x

for _ in range(int(input())):
    x = int(input())

    if x < 10**4:
        for i in range(x):
            if verify(x, i):
                print(i)
                break
        else:
            print(-1)
    else:
        for i in range(10**4):
            y = random.randint(0, x)
            if verify(x, y):
                print(y)
                break
        else:
            print(-1)