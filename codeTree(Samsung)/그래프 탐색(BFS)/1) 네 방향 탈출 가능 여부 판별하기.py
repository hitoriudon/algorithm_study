from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (m)] for _ in range (n)]
queue = deque()

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs(x, y): # dxs, dys의 순서를 변경하게 되면, grid 값이 달라진다. 영향을 끼침.
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북
    # dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서
    order = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = True
                order += 1
                grid[nx][ny] = order
                queue.append((nx, ny))
                
x, y = 0, 0 # start position
visited[x][y] = True
queue.append((x, y))

bfs(0, 0)
print(1 if grid[n - 1][m - 1] > 1 else 0)
for line in grid:
    for num in line:
        print(num, end=" ")
    print()
print()