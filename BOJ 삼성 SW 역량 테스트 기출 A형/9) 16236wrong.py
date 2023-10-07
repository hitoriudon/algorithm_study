# 16236, 아기 상어, G3
from collections import deque

grid = [
    [4,3,2,1],
    [0,0,0,0],
    [0,0,9,0],
    [1,2,3,4]
]
level = 2
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
def is_range(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4
answer = [(0, 3), (3, 0)]
temp = []
def bfs(x, y, t):
    queue = deque()
    x, y, t = 2, 2, 0
    queue.append((x, y, t))
        
    while queue:
        x, y, t = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and grid[nx][ny] != -1 and level >= grid[nx][ny]:
                x, y = nx, ny
                grid[x][y] = -1
            if (x, y) in answer:
                temp.append((x, y, t + 1))
            else:
                queue.append((x, y, t + 1))
            print(temp)
                
bfs(2,2,0)
print(temp)