import sys
from itertools import accumulate

sys.stdin = open('maxcross.in', 'r')
sys.stdout = open('maxcross.out', 'w')

# read the input

N, K, B = map(int, input().split())

A = [0] * (N + 1)

for _ in range(B):
    A[int(input())] = 1
# make a, its prefix sum

A = list(accumulate(A))

anws = float('inf')


for i in range(len(A)):
    if i + K <= N:
        anws = min(anws, A[i + K] - A[i])

print(anws)
