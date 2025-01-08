x, y = 0,0

with open('lostcow.in', "r") as f:
    x, y = map(int, f.readline().strip().split())


neg = False
greater = False

if x > y:
    greater = True

steps = 0
num = 1

while x < y if not greater else x > y:
    if not neg:
        x += num
        neg = True
    else:
        x -= num
        neg = False


    otherNum = num + num * 2
    if x < y if not greater else x > y:
        steps += num
        num = otherNum
    else:
        steps += abs(x - y)
        break

    num *= 2
    






with open('lostcow.out', "w") as f:
    f.write(str(steps) + "\n")