import sys

# sys.stdin = open('sort.in', 'r')
# sys.stdout = open('sort.out', 'w')

# N = int(input())
# A = [int(input()) for _ in range(N)]

cnt = 0

N = 5
A = [1, 2, 4, 3, 5]

sorted_A = False

while not sorted_A:
    sorted_A = True
    cnt += 1

    for i in range(N - 1):
        if A[i + 1] < A[i]:
            A[i], A[i + 1] = A[i + 1], A[i]
            sorted_A = False


print(cnt)