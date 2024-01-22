from collections import deque

def is_range(x, y, n, m):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs(w, h):
    dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    
    while dq:
        x, y = dq.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_range(nx, ny, h, w) and not visited[nx][ny] and grid[nx][ny] == 1:
                dq.append((nx, ny))
                visited[nx][ny] = True

while True:    
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit(0)
    
    grid = [list(map(int, input().split())) for _ in range (h)]
    visited = [[False for _ in range (w)] for _ in range (h)]
    dq = deque()
    
    land = 0
    for x in range (h):
        for y in range (w):
            if grid[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                dq.append((x, y))
                bfs(w, h)
                land += 1
    print(land)
    