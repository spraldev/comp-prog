import sys
# sys.setrecursionlimit(10**6)
# sys.stdin = open('shuffle.in', 'r')
# sys.stdout = open('shuffle.out', 'w')


N = int(input())
A = list(map(int, input().split()))
next_node = [0] * (N + 1)

for i in range(N):
	next_node[i] = A[i] - 1


def count_cyclic_nodes(graph):
    cyclic_nodes = set()
    visited = set()

    for start_node in range(len(graph)):
        if start_node not in visited:
            tortoise = start_node
            hare = graph[start_node]

            while hare != tortoise and hare is not None:
                if hare in visited:
                    tortoise = -1
                    break
                tortoise = graph[tortoise]
                hare = graph[graph[hare]] if graph[hare] is not None else None

            if hare is not None and tortoise != -1:
                tortoise = start_node
                while tortoise != hare:
                    tortoise = graph[tortoise]
                    hare = graph[hare]
                
                temp = start_node
                while temp != hare:
                    cyclic_nodes.add(temp)
                    temp = graph[temp]
                cyclic_nodes.add(hare)

            visited.add(start_node)

    return len(cyclic_nodes)

print(count_cyclic_nodes(next_node))