import sys
from itertools import accumulate

sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')

N = int(input())
A = []

for _ in range(N):
    A.append(int(input()))

prefix = [x % 7 for x in list(accumulate(A))]
sett = list(set(prefix))
maximum = 0

for i in sett:
    first = prefix.index(i)
    last = N - prefix[::-1].index(i) - 1
    maximum = max(maximum, last - first)

print(maximum)