from collections import deque

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs(x, y):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 1: # 1인 경우가 못 가는 거임
                visited[nx][ny] = True
                queue.append((nx, ny))
                    
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (n)] for _ in range (n)]

dots = []
for _ in range (k):
    r, c = map(int, input().split())
    dots.append((r - 1, c - 1)) # index 보정
    
for x, y in dots:    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    bfs(x, y)

ans = 0
for line in visited:
    ans += line.count(True)    
print(ans)