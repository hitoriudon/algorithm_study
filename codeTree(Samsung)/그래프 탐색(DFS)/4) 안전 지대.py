import sys
from copy import deepcopy
sys.setrecursionlimit(2500) # 없으면 에러 남

def find_the_maximum_value_of_k(graph):
    tmp = 0
    for line in graph:
        tmp = max(tmp, max(line))
    return tmp

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def raining(graph, rain):
    for i in range (n):
        for j in range (m):
            graph[i][j] -= rain
            if graph[i][j] < 0:
                graph[i][j] = 0
    return graph

def dfs(x, y):
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and not visited[nx][ny] and test_grid[nx][ny] > 0:
            visited[nx][ny] = True
            dfs(nx, ny)

# main
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
k = find_the_maximum_value_of_k(grid)

ans = 0
max_rain = 1
for rain in range (1, k + 1):
    max_num = 0 
    test_grid = raining(deepcopy(grid), rain)
    visited = [[False for _ in range (m)] for _ in range (n)]
    
    # 시작점 찾기
    for x in range (n):
        for y in range (m):
            if test_grid[x][y] > 0 and not visited[x][y]:
                visited[x][y] = True
                dfs(x, y)
                max_num += 1
    if ans < max_num:
        ans = max_num
        max_rain = rain
        
print(max_rain, ans)