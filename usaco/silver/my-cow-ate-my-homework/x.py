import sys

sys.stdin = open('homework.in', 'r')
sys.stdout = open('homework.out', 'w')

N = int(input())
A = list(map(int, input().split()))

dictr = {}



for i in range(N):
    arr_length = N - i - 1
    if arr_length < 3:
        continue

    avg = total / arr_length
    dictr[i + 1] = avg

# get all keys with max value
max_avg = max(dictr.values())
scores = [k for k, v in dictr.items() if v == max_avg]
print(*scores)