spotty_cows = []
plain_cows = []

N, M = 0, 0


with open('cownomics.in', 'r') as f:
    N, M = map(int, f.readline().strip().split())
    for i in range(N):
        spotty_cows.append(f.readline().strip())
    for i in range(N):
        plain_cows.append(f.readline().strip())

anws = 0


for i in range(M):
    spotty = []
    plain = []

    for j in range(N):
        spotty.append(spotty_cows[j][i])
        plain.append(plain_cows[j][i])

    if set(spotty) & set(plain) == set():
        anws += 1


with open('cownomics.out', 'w') as f:
    f.write(str(anws) + '\n')