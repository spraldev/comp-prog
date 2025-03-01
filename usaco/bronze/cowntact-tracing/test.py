from itertools import permutations


N = int(input())
cow_heights = list(map(int, input().split()))
height_lims = list(map(int, input().split()))


perms = list(permutations(cow_heights, N))

count = 0

for perm in perms:
    passed = True

    for i in range(N):
        if perm[i] > height_lims[i]:
            passed = False
            break

    if passed:
        count += 1

print(count)

    