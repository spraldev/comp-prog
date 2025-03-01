def solve():
    import sys
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    a = list(map(int, data[1:]))

    # 1-based indexing for convenience
    # a[i]   will be the offset of patch i, i in [1..N]
    a = [0] + a  # pad so that a[1] corresponds to the first patch

    # prefix1[i] = x_1 + x_2 + ... + x_i
    # prefix2[i] = (0)*x_1 + (1)*x_2 + ... + (i-1)*x_i
    prefix1 = [0]*(N+1)
    prefix2 = [0]*(N+1)

    cost = 0

    for i in range(1, N+1):
        # current offset e_i = a[i] + sum_{k=1..i-1} [- x_k * (i-k+1)]
        # but that sum is - [ i*prefix1(i-1) - prefix2(i-1) ]
        # => e_i = a[i] - ( i*prefix1[i-1] - prefix2[i-1] )
        e_i = a[i] - ( i*prefix1[i-1] - prefix2[i-1] )

        cost += abs(e_i)

        # We fix patch i by applying e_i "units" of remove (if e_i>0) or add (if e_i<0).
        # That means x_i = e_i in our notation.
        x_i = e_i

        # Update prefix sums for future patches (i+1..N)
        prefix1[i] = prefix1[i-1] + x_i
        prefix2[i] = prefix2[i-1] + (i-1)*x_i

    print(cost)

solve()