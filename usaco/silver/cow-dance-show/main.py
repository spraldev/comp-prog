from heapq import heapify, heappop
import sys

sys.stdin = open('cowdance.in', 'r')
sys.stdout = open('cowdance.out', 'w')

N, T = map(int, input().split())
cows = [int(input()) for _ in range(N)]

def res(k):
    stage = cows[:k]
    heap = [x for x in range(k, N)]
    heapify(heap)

    while heap:
        val = min(stage)

        for i in range(len(stage)):
            stage[i] -= val

        for i in range(len(stage)):
            if stage[i] == 0:
                if heap:
                    stage[i] = cows[heappop(heap)]
                else:
                    break

        if val + max(stage) > T:
            return val + max(stage)
        
    return val + max(stage)

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