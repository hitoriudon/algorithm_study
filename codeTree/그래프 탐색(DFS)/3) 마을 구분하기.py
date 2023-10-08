n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (n)] for _ in range (n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북

village = [] # answer list

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def dfs(x, y):
    global cnt
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
            cnt += 1
            grid[nx][ny] = cnt
            visited[nx][ny] = True
            dfs(nx, ny)
    
# 시작 좌표 완전 탐색
for x in range (n):
    for y in range (n):
        if grid[x][y] == 1:
            cnt = 0
            visited[x][y] = True
            cnt += 1
            dfs(x, y)
            village.append(cnt)

print(len(village))
for people in sorted(village):
    print(people)