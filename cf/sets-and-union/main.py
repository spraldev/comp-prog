for _ in range(int(input())):
    N = int(input())
    sets = [set(list(map(int, input().split()))[1:]) for _ in range(N)]

?
    anws = 0
    max_set = set()

    if N == 1:
        print(0)
        continue
    # all sets are equal to each other
    if len({frozenset(s) for s in sets}) == 1:
        print(0)
        continue

    for i in range(N):
        if len(sets[i]) > len(max_set):
            max_set = sets[i]

    Bad_set = sets[0]

    for set_i in sets:
        Bad_set = Bad_set | set_i


    for i in range(N):
        x = 0
        max_copy = max_set.copy()

        for j in sets:
            if len(max_set.union(j)) > x and max_copy.union(j) != Bad_set:
                x = len(max_copy.union(j))
                max_copy = max_copy.union(j)


        max_set = max_copy

    print(len(max_set))

            
            