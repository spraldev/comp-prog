from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

dic = {}

for i in range(N):
    dic[i+1] = A[i]





for i, j in queries:
    cop = A.copy()
    
    cop[i - 1] = j
    cop.sort()
    

    copSum = 0

    for i in range(1, N + 1):
        copSum += i * cop[i - 1]

    print(copSum)
