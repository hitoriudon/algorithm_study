# 인접 리스트를 활용한 풀이
n, m = map(int, input().split())
graph = [[] for _ in range (n + 1)]
visited = [False for _ in range (n + 1)]

for _ in range (m):
    n1, n2 = map(int, input().split())
    graph[n2].append(n1)
    graph[n1].append(n2)

ans = 0 
def dfs(node):
    global ans
    for current in graph[node]:
        if not visited[current]:
            ans += 1
            visited[current] = True
            dfs(current)

visited[1] = True
dfs(1)
print(ans)