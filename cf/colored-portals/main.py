
for _ in range(int(input())):
    N, Q = map(int, input().split())
    cities = input().split()


    adj = [set() for _ in range(N)]
    last_occurrence = {letter: -1 for letter in "BGRY"}

    for i, city in enumerate(cities):
        for letter in city:
            if last_occurrence[letter] != -1:
                j = last_occurrence[letter]
                adj[j].add(i)
                adj[i].add(j)
            last_occurrence[letter] = i

    arr = ["BG", "BR", "BY", "GR", "GY", "RY"]
    arr = set(arr)

    
    for _q in range(Q):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        u_t = cities[u]
        v_t = cities[v]


        if u_t[0] in v_t or u_t[1] in v_t:
            print(abs(u - v))
            continue

        poss = []

        for i in range(2):
            for j in range(2):
                if u_t[i] + v_t[j] in arr:
                    poss.append(u_t[i] + v_t[j])

        passed = False
        ans = float("inf")

        for i in poss:
            if i in adj[u] and i in adj[v]:
                passed = True
                ans = min(ans, abs(u - v))
                
        if passed:
            print(ans)
        else:
            print(-1)




