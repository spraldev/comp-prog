def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    cows = []
    for _ in range(N):
        x = int(next(it)); y = int(next(it))
        cows.append((x, y))
    # Sort cows by x–coordinate.
    cows.sort(key=lambda p: p[0])
    # Build Y: list of y–values in x–order.
    ys = [p[1] for p in cows]
    # Rank the y–values (they are distinct).
    sorted_ys = sorted(ys)
    rank = {}
    for i, val in enumerate(sorted_ys):
        rank[val] = i
    Y = [rank[y] for y in ys]
    
    n = N
    # Build F_cols: a list of (n+1) lists, each of length n+1.
    # For each 0 <= v <= n, F_cols[v][i] is the number of cows among the first i cows (in x–order)
    # having y–rank < v.
    F_cols = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        r = Y[i]
        # For v <= r, the indicator is 0; for v > r it is 1.
        # Copy previous cumulative sums then update.
        # First, for v from 0 to r (inclusive), no addition.
        for v in range(r + 1):
            F_cols[v][i + 1] = F_cols[v][i]
        # Then, for v from r+1 to n, add 1.
        for v in range(r + 1, n + 1):
            F_cols[v][i + 1] = F_cols[v][i] + 1

    total = 0
    # Now, for every x-interval [i, j], compute:
    #   cnt = j - i + 1, the number of cows in that interval.
    #   pos_i = (# cows in interval with y < Y[i])
    #   pos_j = (# cows in interval with y < Y[j])
    # and add (min(pos_i, pos_j)+1) * (cnt - max(pos_i, pos_j)).
    for i in range(n):
        Yi = Y[i]
        for j in range(i, n):
            cnt = j - i + 1
            pos_i = F_cols[Yi][j + 1] - F_cols[Yi][i]
            Yj = Y[j]
            pos_j = F_cols[Yj][j + 1] - F_cols[Yj][i]
            if pos_i < pos_j:
                mi = pos_i
                ma = pos_j
            else:
                mi = pos_j
                ma = pos_i
            total += (mi + 1) * (cnt - ma)
    # Add 1 for the empty subset.
    total += 1
    sys.stdout.write(str(total))

if __name__ == '__main__':
    solve()
