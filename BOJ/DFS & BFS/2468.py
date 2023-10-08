# 2468, 안전 영역, S1
from copy import deepcopy
import sys
sys.setrecursionlimit(1000000)

def find_the_maximum_of_k(graph):
    tmp = 0
    for line in graph:
        tmp = max(tmp, max(line))
    return tmp

def raining(graph, rain):
    for i in range (n):
        for j in range (n):
            graph[i][j] -= rain
            if graph[i][j] < 0:
                graph[i][j] = 0
    return graph

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def dfs(x, y):
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and not visited[nx][ny] and test_grid[nx][ny] > 0:
            visited[nx][ny] = True
            dfs(nx, ny)
    
n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]
rain_range = find_the_maximum_of_k(grid)

ans = 0
for i in range (rain_range + 1): # 아무 곳도 안 잠길 수 있다는 말이 비가 아예 안 올 수도 있다는 말이었구나
    test_grid = deepcopy(grid)
    visited = [[False for _ in range (n)] for _ in range (n)]
    test_grid = raining(test_grid, i)
    
    safe_area = 0
    for x in range (n):
        for y in range (n):
            if test_grid[x][y] > 0 and not visited[x][y]:
                visited[x][y] = True
                dfs(x, y)
                safe_area += 1
    # print(safe_area, i)
    # for line in test_grid:
    #     for num in line:
    #         print(num, end=" ")
    #     print()
    # print()
    ans = max(ans, safe_area)
print(ans)