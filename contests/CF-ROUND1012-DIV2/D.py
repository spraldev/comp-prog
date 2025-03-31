import sys, math

L = 150000
is_prime = [True] * (L + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(L**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, L + 1, i):
            is_prime[j] = False


output_lines = []

for _ in range(int(input())):
    n = int(input())
    m = max(1, int(n ** (1 / 3)))
    prefix = []
    used = [False] * (n + 1)
    S = 0
    
    for i in range(1, m + 1):
        chosen = None
        for x in range(1, n + 1):
            if not used[x]:
                avg = (S + x + i - 1) // i
                if avg <= L and is_prime[avg]:
                    chosen = x
                    break
        if chosen is None:
            for x in range(1, n + 1):
                if not used[x]:
                    chosen = x
                    break
        prefix.append(chosen)
        used[chosen] = True
        S += chosen

    remaining = []
    for x in range(1, n + 1):
        if not used[x]:
            remaining.append(x)
    perm = prefix + remaining
    print(" ".join(map(str, perm)))
