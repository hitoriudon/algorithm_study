from collections import deque
from copy import deepcopy

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

ans = 0
def bfs(graph):
    global ans
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
    visited = [[False for _ in range (n)] for _ in range (n)]

    # 큐에 시작점 다 넣어놓기
    queue = deque()
    for i in range (k):
        x, y = start_dots[i]
        visited[x][y] = True
        queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
    count = 0
    for line in visited:
        count += line.count(True)
    ans = max(ans, count)
    
def remove_stones(dots):
    temp_grid = deepcopy(grid)
    for x, y in dots:
        temp_grid[x][y] = 0
    return temp_grid
    
def make_combinations(level, begin):
    if level == stone:
        test_grid = remove_stones(stones)
        bfs(test_grid)
        return
    
    for i in range (begin, len(stone_location)):
        stones[level] = stone_location[i]
        make_combinations(level + 1, i + 1)

n, k, stone = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
start_dots = []
for _ in range (k):
    r, c = map(int, input().split())
    start_dots.append((r - 1, c - 1)) # 인덱스 보정
    
stone_location = []
stones = [(0, 0) for _ in range (stone)]

# 돌이 있는 곳 좌표 탐색
for i in range (n):
    for j in range (n):
        if grid[i][j] == 1:
            stone_location.append((i, j))
make_combinations(0,0)

print(ans)