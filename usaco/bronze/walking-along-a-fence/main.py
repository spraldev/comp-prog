N, P = list(map(int, input().split()))
cows = []
posts = []

for i in range(P):
    posts.append(tuple(map(int, input().split())))

for i in range(N):
    cows.append(tuple(map(int, input().split())))

posts.sort()

for cow in cows:

    leftDist = 0
    rightDist = 0

    