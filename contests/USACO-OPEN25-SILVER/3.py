N = int(input())

graph = {i: [] for i in range(1, N+1)}
diffandEnjoy = {}

for i in range(2, N+1):
    p, d, e = map(int, input().split())
    graph[i] = [p]
    diffandEnjoy[i] = (d, e)

# Precompute best paths for different jump counts


paths = {i: [] for i in range(1, N+1)} 
enjoyment = {i: [] for i in range(1, N+1)} 
diffs = {i: [] for i in range(1, N+1)} 

def precomp(node, cur_path, cur_enj, cur_diffs):

    if node == 1:
        paths[cur_path[0]] = cur_path.copy()
        enjoyment[cur_path[0]] = cur_enj.copy()
        diffs[cur_path[0]] = cur_diffs.copy()
        return
    
    for neighbor in graph[node]:

        if neighbor not in cur_path:
            cur_path.append(neighbor)

            if node != 1:
                diff, enjoy = diffandEnjoy[node]
                cur_enj.append(enjoy)
                cur_diffs.append(diff)
            precomp(neighbor, cur_path, cur_enj, cur_diffs)
            cur_path.pop()

            if node != 1:
                cur_enj.pop()
                cur_diffs.pop()


for i in range(2, N+1):
    precomp(i, [i], [], [])


for _ in range(int(input())):
    s, c = map(int, input().split())
    ans = 0
    

    for node in range(2, N+1):
        if not paths[node]: 
            continue
            
        # count jumps and calculate enjoyment
        jumps = sum(1 for diff in diffs[node] if diff > s)

        if jumps <= c:
            ans = max(ans, sum(enjoyment[node]))
    
    print(ans)
