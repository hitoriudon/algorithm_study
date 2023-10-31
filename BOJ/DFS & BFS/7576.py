# 7576, 토마토, G5, BFS
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (m)] for _ in range (n)]

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs():
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] # 남 동 북 서
    
    while queue:
        x, y, time = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                grid[nx][ny] = time + 1
                queue.append((nx, ny, time + 1))
    
queue = deque()

for i in range (n):
    for j in range (m):
        if grid[i][j] == 1:
            visited[i][j] = True
            queue.append((i, j, 0))
            grid[i][j] = 0
bfs()   

ans = 0
for i in range (n):
    for j in range (m):
        ans = max(ans, grid[i][j])

all_tomato = True

for i in range (n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] == 0:
            all_tomato = False
            break

print(ans if all_tomato else -1)
