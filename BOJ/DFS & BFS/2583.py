from collections import deque

def is_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

def bfs():
    global ans
    
    cnt = 1
    while que:
        x, y = que.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = True
                que.append((nx, ny))
    
    arr.append(cnt)
    ans += 1

m, n, shapes = map(int, input().split())
grid = [[0 for _ in range (n)] for _ in range (m)]

for _ in range (shapes):
    sx, sy, ex, ey = map(int, input().split())
    
    for y in range (sy, ey):
        for x in range (sx, ex):
            grid[y][x] = 1

visited = [[False for _ in range (n)] for _ in range (m)]
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

que = deque()            

ans = 0
arr = []
for i in range (m):
    for j in range (n):
        if grid[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            que.append((i, j))
            bfs()

print(ans)

for num in sorted(arr):
    print(num, end=" ")