from collections import deque

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs():
    dxs, dys = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
    
    while queue:
        x, y, value = queue.popleft()   
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                grid[nx][ny] = value + 1
                queue.append((nx, ny, value + 1))

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1 # 인덱스 보정
grid = [[0 for _ in range (n)] for _ in range (n)]
visited = [[False for _ in range (n)] for _ in range (n)]

queue = deque()
visited[r1][c1] = True
queue.append((r1, c1, 0))
bfs()
ans = grid[r2][c2]
print(ans if visited[r2][c2] else -1)