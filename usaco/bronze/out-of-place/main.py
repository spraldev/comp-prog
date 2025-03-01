N = 0
cows = []

with open('outofplace.in', 'r') as f:
    N = int(f.readline())
    for i in range(N):
        cows.append(int(f.readline()))

swaps = 0


for i in range(N):
    if cows[i] != sorted(cows)[i]:
        swaps += 1



with open('outofplace.out', 'w') as f:
    f.write(str(swaps-1))
