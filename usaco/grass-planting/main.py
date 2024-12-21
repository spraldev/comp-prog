from collections import deque

n = 0
connections = []

with open("planting.in", "r") as f:
    n = int(f.readline())
    for _ in range(n - 1):
        u, v = map(int, f.readline().split())
        connections.append((u, v))

def add_edge(graph, node1, node2):
    graph.setdefault(node1, []).append(node2)
    graph.setdefault(node2, []).append(node1)

def build_graph(edges):
    graph = {}
    for node1, node2 in edges:
        add_edge(graph, node1, node2)
    return graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    count = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
            print(queue, visited)
            count += 1
    return count

graph = build_graph(connections)

count = bfs(graph, 1)

with open("planting.out", "w") as f:
    f.write(str(count - 1))
