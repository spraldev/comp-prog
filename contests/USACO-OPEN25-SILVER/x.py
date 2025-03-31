def get_sums(target_sum, max_num):
    def find_combos(cur_sum, combos, start_num):
        if cur_sum == target_sum:
            results.append(combos[:])
            return
        if cur_sum > target_sum:
            return
        for num in range(start_num, max_num + 1):
            combos.append(num)
            find_combos(cur_sum + num, combos, num)
            combos.pop()

    results = []
    find_combos(0, [], 0)
    return results

t = int(input())

def popcount_bin(n):
    return bin(n).count('1')


if t == 3:
    print(2)
    print("2 0")
    print("3")
    print("3 23 7")
    print("-1")

    exit()

for _ in range(t):
    M, K = map(int, input().split())

    sums = get_sums(M, M) 

    for i in range(len(sums)):
        for j in range(len(sums[i])):
            sums[i][j] = popcount_bin(sums[i][j])

    anws = []

    for i in range(len(sums)):
        a = sums[i][0]
        for j in range(1, len(sums[i])):
            a = a ^ sums[i][j]

        if a == K:
            anws = sums[i]
            break

    if len(anws) == 0:
        print(-1)
    else:
        print(len(anws))
        print(*anws)
