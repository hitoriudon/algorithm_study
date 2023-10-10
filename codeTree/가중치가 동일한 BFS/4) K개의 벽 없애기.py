from collections import deque
from copy import deepcopy

def find_wall():
    temp = []
    for i in range (n):
        for j in range (n):
            if grid[i][j] == 1:
                temp.append((i, j))
    return temp

def remove_wall(walls):
    temp_grid = deepcopy(grid)
    
    for x, y in walls:
        temp_grid[x][y] = 0
        
    return temp_grid

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

ans = 100000 # max size
def bfs(graph):
    global ans
    queue = deque()
    queue.append((start_x - 1, start_y - 1, 0))
    visited = [[False for _ in range (n)] for _ in range (n)]
    visited[start_x - 1][start_y - 1] = True
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while queue:
        x, y, value = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx, ny, value + 1))
                if nx == end_x - 1 and ny == end_y - 1:
                    ans = min(ans, value + 1)

def make_combinations(level, begin):
    if level == k:
        test_grid = remove_wall(wall)
        bfs(test_grid)
        return
    
    for i in range (begin, len(dots)):
        wall[level] = dots[i]
        make_combinations(level + 1, i + 1)
        
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]

start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())

grid[end_x - 1][end_y - 1] = -1 # 도착지점 표시

# 벽 조합 만들고 시작
wall = [(0, 0) for _ in range (k)]
dots = find_wall()
make_combinations(0, 0)
print(ans if ans != 100000 else -1)