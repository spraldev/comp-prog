import sys

sys.stdin = open('bcount.in', 'r')
sys.stdout = open('bcount.out', 'w')

N, Q = map(int, input().split())
A = [int(input()) for _ in range(N)]

sum1 = [0]
sum2 = [0]
sum3 = [0]

for i in A: sum1.append(sum1[-1] + (i == 1)); sum2.append(sum2[-1] + (i == 2)); sum3.append(sum3[-1] + (i != 1 and i != 2))

queries = [tuple(map(int, input().split())) for _ in range(Q)]

for l, r in queries:
    print(sum1[r] - sum1[l - 1], sum2[r] - sum2[l - 1], sum3[r] - sum3[l - 1])