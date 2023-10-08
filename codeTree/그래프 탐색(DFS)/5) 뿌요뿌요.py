n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (n)] for _ in range (n)]
BLOCK_COUNT = 4

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def dfs(x, y, num):
    global same_block
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == num:
            same_block += 1
            visited[nx][ny] = True
            dfs(nx, ny, num)
    
ans = []
block = 0
for x in range (n):
    for y in range (n):
        same_block = 1
        if not visited[x][y]:
            visited[x][y] = True
            value = grid[x][y]
            dfs(x, y, value)
            if same_block >= BLOCK_COUNT:
                block += 1
            ans.append(same_block)

print(block, max(ans))