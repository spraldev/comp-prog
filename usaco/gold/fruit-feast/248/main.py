import sys

# sys.stdin = open('248.in', 'r')
# sys.stdout = open('248.out', 'w')

N = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)]

a = []
for i in range(N):
    b = int(input())
    dp[i][i] = b
    a.append(b)


ans = 0

for i in range(N):
    for j in range(i + 1, N):
        prev = dp[i][j - 1]

        if a[j] == prev:
            dp[i][j] = prev + 1
        else:
            dp[i][j] = prev

        ans = max(ans, dp[i][j])


print(ans)