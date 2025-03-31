import sys

sys.setrecursionlimit(10**6)

def dfs(node, adj, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, component)

def get_connected_components(adj, N):
    visited = [False] * (N + 1)
    components = []
    
    for node in range(1, N + 1):
        if not visited[node]:
            current_component = []
            dfs(node, adj, visited, current_component)
            components.append(current_component)
    
    return components


def find_closest(arr, target):
    if not arr:
        return None

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if high < 0:
      return arr[low]
    if low >= len(arr):
      return arr[high]
    
    if abs(arr[low] - target) < abs(arr[high] - target):
        return arr[low]
    else:
        return arr[high]


def find_closest_2_elements(a, b):
    if len(a) < len(b):
        smaller, larger = a, b
    else:
        smaller, larger = b, a

    min_diff = float('inf')

    for x in smaller:
        min_diff = min(min_diff, abs(x - find_closest(larger, x)))
        
    return min_diff



for _ in range(int(input())):
    N, M = map(int, input().split())
    adj = {i: [] for i in range(1, N + 1)}

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    comps = get_connected_components(adj, N)

    for comp in comps:
        comp.sort()
    

    for comp in comps:
        if 1 in comp and N in comp:
            print(0)
            break
    else:
        anws = float('inf')
        barn1_comp = None
        barnN_comp = None
        other_comps = []
        
        for comp in comps:
            if 1 in comp:
                barn1_comp = comp
            elif N in comp:
                barnN_comp = comp
            else:
                other_comps.append(comp)

        for comp in other_comps:
            anws = min(anws, find_closest_2_elements(barn1_comp, comp)**2 + 
                      find_closest_2_elements(barnN_comp, comp)**2)

        anws = min(anws, find_closest_2_elements(barn1_comp, barnN_comp)**2)

        print(anws)