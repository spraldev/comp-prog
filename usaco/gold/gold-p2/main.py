MOD = 10**9 + 7

import math


K, N, L = map(int, input().split())
T = input()


ans = 0
cnt = 0

for i in range(N -1, -1, -1):

    if T[i] == "O":
        cnt += 1
    elif cnt >= K:
        ans += math.comb(cnt, K)


print(ans**L % MOD)
