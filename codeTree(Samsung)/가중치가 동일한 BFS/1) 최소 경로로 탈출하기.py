from collections import deque

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
    
    while queue:
        x, y, dist = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                grid[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (m)] for _ in range (n)]
queue = deque()
queue.append((0, 0, 0))
visited[0][0] = True

bfs()
ans = grid[n - 1][m - 1]
print(ans if ans > 1 else -1)