def dfs(node):
    global answer
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            answer += 1
            dfs(i)
    
n = int(input())
m = int(input())
answer = 0
graph = [[] for _ in range (n+1)]
visited = [False] * (n+1)
for _ in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for line in graph:
    line.sort()
dfs(1)
print(answer)