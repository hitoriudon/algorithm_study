# 14940, 쉬운 최단거리, S1
from collections import deque

def find_the_start_point(graph):
    for i in range (n):
        for j in range (m):
            if graph[i][j] == 2:
                return (i, j)
    
def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
    
    while queue:
        x, y, value = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                grid[nx][ny] = value
                visited[nx][ny] = True
                queue.append((nx, ny, value + 1))
  
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (m)] for _ in range (n)]
queue = deque()

x, y = find_the_start_point(grid)
visited[x][y] = True
grid[x][y] = 0
queue.append((x, y, 1)) # 그 다음부턴 1 채워 넣어야지
bfs()

for i in range (n):
    for j in range (m):
        if grid[i][j] == 1 and not visited[i][j]:
            grid[i][j] = -1

for line in grid:
    for num in line:
        print(num, end=" ")
    print()