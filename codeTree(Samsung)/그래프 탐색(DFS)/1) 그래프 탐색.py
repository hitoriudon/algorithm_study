# 2차원 그래프를 활용한 풀이

n, m = map(int, input().split())
graph = [[0 for _ in range (n + 1)] for _ in range (n + 1)]
visited = [False for _ in range (n + 1)]
for _ in range (m):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

ans = 0
def dfs(node):
    global ans
    for current in range (1, n+1):
        if graph[node][current] == 1 and not visited[current]:
            ans += 1
            visited[current] = True
            dfs(current)
            
visited[1] = True
dfs(1)
print(ans)