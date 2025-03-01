import sys
sys.stdin = open('cowdance.in', 'r')
sys.stdout = open('cowdance.out', 'w')


N, T = map(int, input().split())
cows = [int(input()) for _ in range(N)]

def res(k):
    init = cows[:k]
    other = cows[k:]

    init.sort()
    time = init[0]

    init = [x - time for x in init]

    i = 0

    while len(other) > 0:
        init.sort()
        zeroCount = init.count(0)
        for j in range(zeroCount):
            if other:
                otherCow = other.pop(0)
                init[init.index(0)] = otherCow
            else:
                break

        if time + max(init) > T:
            return time + max(init)

        init.sort()
        time += init[0]
        newTime = init[0]
        init = [x - newTime for x in init]

    return time + max(init)

anws = 0

lo = 1
hi = N

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if res(mid) <= T:
        hi = mid - 1
        anws = mid
    else:
        lo = mid + 1

print(anws)