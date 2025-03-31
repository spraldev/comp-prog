import sys

sys.stdin = open("pairup.in", "r")
sys.stdout = open("pairup.out", "w")


# read our input
N = int(input())

cows = []

for i in range(N):
    X, Y = map(int, input().split())
    cows.append(list((Y, X)))

cows.sort()

# two pointer stuff

i, j = 0, len(cows)-1
anws = 0

while i < j:
    anws = max(anws, cows[i][0] + cows[j][0])

    if cows[i][1] > cows[j][1]:
        cows[i][1] -= cows[j][1]
        j -= 1
    elif cows[i][1] < cows[j][1]:
        cows[j][1] -= cows[i][1]
        i += 1
    else:
        i += 1
        j -= 1

print(anws)