import sys
from bisect import bisect

sys.stdin = open('convention.in', 'r')
sys.stdout = open('convention.out', 'w')

N, M, C = map(int, input().split())

cows = sorted(list(map(int, input().split())))



def check(t):
    bus = 1
    cowCount = 0
    minCow = cows[0]

    for i in range(len(cows)):
        if cowCount == C:
            cowCount = 1
            bus += 1

            minCow = cows[i]

        elif cows[i] - minCow > t:
            cowCount = 1
            bus += 1

            minCow = cows[i]
        else: 
            cowCount += 1


    return bus

lo = 0
hi = max(cows)

anws = 0

while lo <= hi:
    mid = lo + (hi - lo) //2

    if check(mid) <= M:
        anws = mid
        hi = mid-1
    else:
        lo = mid + 1

print(anws)

