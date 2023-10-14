from collections import deque
from copy import deepcopy 
n = int(input())
grid = [list(input()) for _ in range (n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

arr = []
def func(level, begin):
    if level == len(walls):
        if 0 <= len(arr) <= 6:
            bfs(arr)
        return

    arr.append(walls[begin])
    func(level + 1, begin + 1)
    arr.pop()

    func(level + 1, begin + 1)

def bfs(wall):
    global ans
    
    test_grid = deepcopy(grid)
    for wx, wy in wall:
        test_grid[wx][wy] = "."
     
    vis = [[False for _ in range (n)] for _ in range (n)]
    vis[startx][starty] = True
    queue.append((startx, starty))

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not vis[nx][ny] and test_grid[nx][ny] == '.':
                queue.append((nx, ny))
                vis[nx][ny] = True
    
    for i in range (n):
        for j in range (n):
            if not vis[i][j] and test_grid[i][j] == '.':
                return
    if 0 <= len(wall) <= 6:
        ans = min(ans, len(wall))
    
# 벽 배열
walls = []
startx, starty = 0, 0
for i in range (n):
    for j in range (n):
        if grid[i][j] == '#':
            walls.append((i, j))
        elif grid[i][j] == '.':
            startx, starty = i, j # 어느 인덱스든 상관 없음 어차피 다 연결되어 있는지 보는 거라서

ans = len(walls)
queue = deque()

if len(walls) == 0:
    print(0)
else:
    func(0, 0)
    print(ans if ans != len(walls) else -1)