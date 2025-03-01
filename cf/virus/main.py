for _ in range(int(input())):
    N, M = map(int, input().split())

    infected = sorted(list(map(int, input().split())))
    houses = [0] * N

    prot = []
    

    while True:
        intervals = []
        infected.sort()
        houses.sort()

        for i in range(len(infected)-1):
            intervals.append((infected[i], infected[i+1], infected[i+1] - infected[i] + 1))

        if len(intervals) > 0:
            intervals.append((infected[-1], infected[0], infected[0] + N - infected[-1] + 1))
            intervals.sort(key=lambda x: x[2], reverse=True)

            if intervals[0][0]-1 in prot:
                prot.append(intervals[1][0]+1)
            else:
                prot.append(intervals[0][0]-1)

            oldCnt = len(infected)

            for i in intervals:
                if i[0]-1 in prot and i[1]+1 not in prot:
                    infected.append(i[1]+1)
                elif i[1]+1 in prot and i[0]-1 not in prot:
                    infected.append(i[0]-1)

            if oldCnt == len(infected):
                print(len(infected))
                break





