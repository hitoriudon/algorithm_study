n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (m)] for _ in range (n)]
dxs, dys = [0, 1], [1, 0] # 우, 하

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def is_snake(x, y):
    return grid[x][y] == 0

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and not is_snake(nx, ny) and not visited[nx][ny]:
            grid[nx][ny] = nx + ny + 1 # check용.. 그냥 경로 확인하고 싶어서
            visited[nx][ny] = True
            dfs(nx, ny)

visited[0][0] = True
dfs(0, 0)
print(1 if visited[n - 1][m - 1] == True else 0)