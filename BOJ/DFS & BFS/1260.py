from collections import deque

def dfs(node):
    visited_dfs[node] = True
    print(node, end=" ")
    for i in graph[node]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(node):
    queue = deque([node])
    visited_bfs[node] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

n, m, start = map(int, input().split())
graph = [[] for _ in range (n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for _ in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for line in graph:
    line.sort()

dfs(start)
print()
bfs(start)