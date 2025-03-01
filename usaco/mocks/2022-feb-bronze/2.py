N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# iterate through B backwards
cnt = 0

for i in range(N-1, -1, -1):
    if a[i] == b[i]:
        continue

    val = b.pop(i)
    ind = a.index(val)
    b.insert(ind, val)
    cnt += 1

print(cnt)

