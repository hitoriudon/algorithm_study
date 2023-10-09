from collections import deque

def how_many_ices():
    ice = 0
    for line in grid:
        ice += line.count(1)
    
    return ice

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs():
    queue = deque()
    visited = [[False for _ in range (m)] for _ in range (n)]
    queue.append((0, 0)) # 시작점
    visited[0][0] = True
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
   
    # 물 부분 찾기
    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    # 녹이기 
    for x in range (n):
        for y in range (m):
            if visited[x][y] == True:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if is_range(nx, ny) and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
    # print()
    # for line in grid:
    #     for num in line:
    #         print(num, end=" ")
    #     print()
    
n, m = map(int, input().split()) 
grid = [list(map(int, input().split())) for _ in range (n)]

ice = 0
time = 0
while True:
    if not how_many_ices():
        break
    ice = how_many_ices()
    bfs()
    time += 1
    
print(time, ice)