N, T = map(int, input().split())

anws = 0
bales = 0
delivs = []
lastDay = 0
lastBalse = 0
lastAnws = 0

for _ in range(N):
    delivs.append(list(map(int, input().split())))


for i in range(1, T+1):
    if delivs and delivs[0][0] == i:
        bales += delivs[0][1]
        delivs.pop(0)

        if bales > 0:
            anws += 1
            bales -= 1

        print("day", i)
        print("bales", bales)
        print("difference in days", i - lastDay)
        print("anwsdiff", anws - lastAnws)

        lastDay = i
        lastBalse = bales
        lastAnws = anws

        print()
        print()


        continue

    if bales > 0:
        anws += 1
        bales -= 1

print(anws)