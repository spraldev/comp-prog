from itertools import accumulate

N = int(input())

L = list(map(int, input().split()))
L = list(accumulate(L))

