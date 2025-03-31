#cow-libi

G, N = map(int, input().split())
grazings = sorted([list(map(int, input().split())) for _ in range(G)])
cows = [list(map(int, input().split())) for _ in range(N)]



def can_cow_reach(cow, grazing):
    return (grazing[2] - cow[2]) **2 >= (grazing[0] - cow[0]) ** 2 + (grazing[1] - cow[1]) ** 2


ans = 0

for cow in cows:
    can_cover_all = True

    # binary search

    lo = 0
    hi = G - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if not can_cow_reach(cow, grazings[mid]):
            break
        else:
            hi = mid - 1


    if not can_cover_all:
        ans += 1


print(ans)
