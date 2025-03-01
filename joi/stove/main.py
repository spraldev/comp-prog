N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]
a.sort()
diff = [a[i+1] - a[i] - 1  for i in range(N-1)]
diff.sort(reverse=True)
cont = a[-1] - a[0] + 1


for i in range(K-1):
    cont -= (diff[i])

print(cont)