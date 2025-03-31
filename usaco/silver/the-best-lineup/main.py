def get_b(A):
    """
    Returns the lexicographically greatest sequence b that can be formed
    if we never perform the "move a cow" operation. This is just the
    usual 'take from the front if it's >= any future cow' logic,
    which can be computed by suffix maxima.
    """
    N = len(A)
    suffix_max = [0] * N
    suffix_max[-1] = A[-1]
    ans = [A[-1]]
    for i in range(N - 2, -1, -1):
        if A[i] >= suffix_max[i + 1]:
            suffix_max[i] = A[i]
            ans.append(A[i])
        else:
            suffix_max[i] = suffix_max[i + 1]
    # Reverse because we collected from the right
    ans.reverse()
    return ans


def try_index(A, differing_index):
    """
    Makes one move: place sorted_A[differing_index] into index `differing_index`.
    Then computes the 'suffix maxima' sequence from that new arrangement.
    """
    N = len(A)
    sorted_A = sorted(A, reverse=True)
    newA = A[:]

    # Attempt to remove sorted_A[differing_index] from a position >= differing_index
    # If not found, remove from anywhere
    try:
        i = newA.index(sorted_A[differing_index], differing_index)
    except ValueError:
        i = newA.index(sorted_A[differing_index])
    
    newA.pop(i)
    newA.insert(differing_index, sorted_A[differing_index])

    suffix_max = [0] * N
    suffix_max[-1] = newA[-1]
    ans = [newA[-1]]
    for i in range(N - 2, -1, -1):
        if newA[i] >= suffix_max[i + 1]:
            suffix_max[i] = newA[i]
            ans.append(newA[i])
        else:
            suffix_max[i] = suffix_max[i + 1]

    ans.reverse()
    return ans


def is_lexographically_greater(A, B):
    """
    Returns True if A is lexicographically greater than B.
    """
    min_len = min(len(A), len(B))
    for i in range(min_len):
        if A[i] > B[i]:
            return True
        elif A[i] < B[i]:
            return False
    # If all compared elements are equal, the longer sequence is considered greater
    return len(A) > len(B)


T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    # 1) Compute the baseline (no move)
    lex_max = get_b(A)
    
    # 2) Identify positions where A differs from sorted(A, reverse=True)
    sorted_A = sorted(A, reverse=True)
    diff_positions = []
    for i in range(N):
        if A[i] != sorted_A[i]:
            diff_positions.append(i)

    # 3) Try moving each differing element up and see if we get a better sequence
    for pos in diff_positions:
        res = try_index(A, pos)
        if is_lexographically_greater(res, lex_max):
            lex_max = res

    # Print the best found
    print(*lex_max)
