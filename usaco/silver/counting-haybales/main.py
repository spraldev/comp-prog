import sys
from bisect import bisect

sys.stdin = open('haybales.in', 'r')
sys.stdout = open('haybales.out', 'w')


N, Q = map(int, input().split())
haybales = sorted(map(int, input().split()))

for _ in range(Q):
    l, r = map(int, input().split())
    print(bisect(haybales, r) - bisect(haybales, l - 1))