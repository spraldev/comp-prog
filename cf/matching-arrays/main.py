import bisect

for _ in range(int(input())):
    n, x = map(int, input().split())
    orig_a = list(map(int, input().split()))
    a = sorted(orig_a)
    b = sorted(list(map(int, input().split())))

    pairs = {}

    ans = 0
    p = False

    for i in b:
        # binary search the first element in a that is greater than i
        idx = bisect.bisect_right(a, i)
        # A[idx] is the first element in A that is greater than i

        if idx > len(a) - 1:
            break
        ans += 1

        if ans == x:
            p = True
            break

        if a[idx] in pairs:
            pairs[a[idx]].append(b[i])
        else:
            pairs[a[idx]] = [b[i]]


    if not p:
        print("NO")
    else:
        print("YES")

        B = [0] * n

        for i in range(len(a)):
            if orig_a[i] in pairs:
                B[i] = pairs[a[i]].pop(0)

        # reconstruct b from pairs






