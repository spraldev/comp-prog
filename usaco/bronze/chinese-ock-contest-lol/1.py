N, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

dif = float('inf')

for i in range(N):
    if i + K > N:
        break


    dif = min(dif, arr[i + K - 1] - arr[i])

print(0 if dif == float('inf') else dif)