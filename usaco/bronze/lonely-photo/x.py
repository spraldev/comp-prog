from itertools import combinations

def find_combinations(N, k):
    return list(combinations(range(N), k))

def inv(e):
    return "D" if e == "R" else "R"


for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    
    
    result = []
    for i in range(1, K+1):
        result += find_combinations(2*N-2, i)

    ne = []

    for i in result:
        lst = ["R"] * (2*N-2)

        for j in range(len(i)):
            lst[i[j]:] = [inv(lst[i[j]])] * (2*N-2 - i[j])

        ne.append(lst)

    for i in result:
        lst = ["D"] * (2*N-2)

        for j in range(len(i)):
            lst[i[j]:] = [inv(lst[i[j]])] * (2*N-2 - i[j])

        ne.append(lst)

    
    for x in ne:
        print("".join(x))

    
    e = set()

    for seq in ne:
        point = (0, 0)
        passed = True

        for char in seq:
            if char == "R":
                point = (point[0], point[1] + 1)
            else:
                point = (point[0] + 1, point[1])

            if point[0] == N-1 and point[1] == N-1:
                passed = True
                break

            if point[0] >= N or point[1] >= N:
                passed = False
                break
                
            if point[0] < N and point[1] < N and arr[point[0]][point[1]] == "H":
                passed = False
                break

        
        if passed:
            e.add(tuple(seq))
            print("".join(seq))

    print(list(e))

        

            

