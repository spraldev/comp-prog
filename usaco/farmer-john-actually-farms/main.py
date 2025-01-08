from bisect import bisect_left

T = int(input())
final_res = []

def ceilingDiv(a, b):
    return (a + b - 1) // b

def countGreater(arr, n, k):
    # same as before
    l = 0
    r = n - 1
    leftMax = n
    while l <= r:
        m = (l + r) // 2
        if arr[m] > k:
            leftMax = m
            r = m - 1
        else:
            l = m + 1
    return n - leftMax

def make_pairs(sorted_plants):
    pairs = []
    for i in range(len(sorted_plants) - 1):
        pairs.append((sorted_plants[i], sorted_plants[i+1]))
    return pairs

def solve(N, heights, growths, M):

    plants_sorted = sorted(range(N), key=lambda i: M[i])
    sorted_plants = [(i, heights[i]) for i in plants_sorted]

    pairs = make_pairs(sorted_plants)
    times = []

    if len(pairs) == 0:
        final_res.append(0)
        return

    for (idx1, h1), (idx2, h2) in pairs:
        g1 = growths[idx1]
        g2 = growths[idx2]

        if h1 > h2:
            times.append(0)
            continue

        growth_diff = g1 - g2
        if growth_diff <= 0:
            times.append(float('inf'))
        else:
            needed = ceilingDiv((h2 - h1 + 1), growth_diff)
            times.append(needed)


    if any(t == float('inf') for t in times):
        final_res.append(-1)
        return

    day_needed = max(times)  


    new_heights = [h + g * day_needed for (h,g) in zip(heights, growths)]


    passT = True
    sorted_final = sorted(new_heights)

    for i, newh in enumerate(new_heights):
        taller_count = countGreater(sorted_final, N, newh)
        if taller_count != M[i]:
            passT = False
            break

    if passT:
        final_res.append(day_needed)
    else:
        final_res.append(-1)

for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    growths = list(map(int, input().split()))
    M = list(map(int, input().split()))

    solve(N, heights, growths, M)

for res in final_res:
    print(res)
