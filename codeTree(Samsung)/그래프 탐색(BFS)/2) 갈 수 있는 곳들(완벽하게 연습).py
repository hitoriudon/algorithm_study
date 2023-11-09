from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (n)] for _ in range (n)]

queue = deque()
for _ in range (k):
    r, c = map(int, input().split())
    queue.append((r - 1, c - 1))
    visited[r - 1][c - 1] = True
    
def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n
def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 1: # 여기선 1이 못 가는 경우임
                visited[nx][ny] = True
                queue.append((nx, ny))

bfs()
ans = 0
for line in visited:
    ans += line.count(True)
print(ans)