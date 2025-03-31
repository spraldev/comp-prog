import sys

sys.stdin = open('262144.in', 'r')
sys.stdout = open('262144.out', 'w')

N = int(input())
a = [int(input()) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(N)]
ans = 0


for i in range(N):
    dp[i][i] = a[i]
    ans = max(ans, dp[i][i])


for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1

        for k in range(i, j):
            if dp[i][k] != -1 and dp[i][k] == dp[k+1][j]:
                dp[i][j] = max(dp[i][j], dp[i][k] + 1)

        ans = max(ans, dp[i][j])

print(ans)
