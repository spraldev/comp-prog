
N, Q = map(int, input().split())
count = 0

xy = [[0] * (N + 1) for _ in range(N + 1)]
zy = [[0] * (N + 1) for _ in range(N + 1)]
arr = [[0] * (N + 1) for _ in range(N + 1)]



def solve():
    global count
    deletion = tuple(map(int, input().split()))
    x = deletion[0]
    yVal = deletion[1]
    z = deletion[2]

    xy[x][yVal] += 1

    if xy[x][yVal] == N:
        count += 1

    zy[z][yVal] += 1

    if zy[z][yVal] == N:
        count += 1

    arr[x][z] += 1

    if arr[x][z] == N:
        count += 1

    print(count)




for i in range(Q):
    solve()