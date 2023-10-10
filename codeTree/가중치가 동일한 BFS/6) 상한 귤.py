from collections import deque

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def find_orange_location():
    for i in range (n):
        for j in range (n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
                visited[i][j] = True

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while queue:
        x, y, value = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, value + 1))
                ans[nx][ny] = value + 1
                # print()
                # for line in visited:
                #     for num in line:
                #         print(num, end=" ")
                #     print()
                
def check(x, y):
    if grid[x][y] == 0:
        ans[x][y] = -1
    elif grid[x][y] == 1:
        ans[x][y] = -2
            
n, orange = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
visited = [[False for _ in range (n)] for _ in range (n)]
queue = deque()
ans = [[0 for _ in range (n)] for _ in range (n)]
find_orange_location()
bfs()

for i in range (n):
    for j in range (n):
        if not visited[i][j]:
            check(i, j)

for line in ans:
    for num in line:
        print(num, end=" ")
    print()