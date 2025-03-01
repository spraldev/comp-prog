def hungarian(cost):
    n = len(cost)
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)

    for i in range(1, n + 1):
        p[0] = i
        minv = [float('inf')] * (n + 1)
        used = [False] * (n + 1)
        j0 = 0
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = float('inf')
            j1 = 0
            for j in range(1, n + 1):
                if not used[j]:
                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    matching = [-1] * n
    for j in range(1, n + 1):
        matching[p[j] - 1] = j - 1
    return matching

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    kings = []
    queens = []

    for _ in range(n):
        row = [int(next(it)) for _ in range(n)]
        kings.append(row)

    for _ in range(n):
        row = [int(next(it)) for _ in range(n)]
        queens.append(row)
    
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cost[i][j] = (kings[i][j] - 1) + (queens[j][i] - 1)

    matching = hungarian(cost)

    for i in range(n):
        print(i + 1, matching[i] + 1)

if __name__ == '__main__':
    main()
