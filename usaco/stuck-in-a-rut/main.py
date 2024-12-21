import sys

f = sys.stdin.read().strip().splitlines()


n = int(f[0].strip())
f = f[1:]


ynums = []
xnums = []


for line in f:
    direction, x, y = line.split()
    xnums.append(int(x))
    ynums.append(int(y))


maxX = max(xnums)
maxY = max(ynums)

arr = [[0] * (maxX + 1) for _ in range(maxY + 1)]
res = [0] * n


for i in range(n):
    line = f[i].split()

    x = int(line[1])
    y = int(line[2])

    arr[y][x] = 2;


for i in range(n):
    line = f[i].split()

    x = int(line[1])
    y = int(line[2])

    if line[0] == "N":
        infinty = False
        for j in range(y + 1, maxY + 1):
            if(arr[j][x] == 1):
                break;

            else:
                arr[j][x] = 1
                res[i] += 1
                
        if infinty:
            res[i] = "Infinity"
    else:
        infinty = False
        for j in range(x + 1, maxX + 1):
            if(arr[y][j] == 1):
                break;
            else:
                arr[y][j] = 1
                res[i] += 1

        if infinty:
            res[i] = "Infinity"

for i in range(n):
    print(res[i])





