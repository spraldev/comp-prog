import sys
from itertools import accumulate

sys.stdin = open('maxcross.in', 'r')
sys.stdout = open('maxcross.out', 'w')


N, K, B = map(int, input().split())

A = [0] * (N + 1)

for i in range(B):
    A[int(input())] = 1


A = list(accumulate(A))

anws = float('inf')

for i in range(len(A)):
    if i + K <= N:
        anws = min(anws, A[i + K] - A[i])

print(anws)