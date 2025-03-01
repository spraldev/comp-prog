from itertools import combinations

N, K = map(int, input().split())

count = 0
N += 1

def calculate(i):
    ste = set()

    for j in combinations(range(N), i):
        ste.add(sum(j))

    return len(ste)
    


# for i in range(K, N + 1):
#     pass

# print(count % (10**9 + 7))

print(calculate(K))