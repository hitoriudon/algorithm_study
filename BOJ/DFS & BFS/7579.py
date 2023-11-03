# 7579, 토마토, G5, BFS (7576 토마토 변형)
# 2차원 그리드 안의 토마토가 아닌, 3차원 속의 토마토
from collections import deque

def is_range(x, y): # 같은 그리드 내의 토마토 범위 체크 함수
    return x >= 0 and x < n and y >= 0 and y < m

def is_up(z): # 위에 토마토 그리드가 있는지
    return z - 1 >= 0

def is_down(z): # 밑에 토마토 그리드가 있는지
    return z + 1 < h

def bfs():
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]   # 동 서 남 북

    while queue:
        z, x, y, t = queue.popleft() # t: time
        
        # up
        if is_up(z) and not visited[z - 1][x][y] and box[z - 1][x][y] == 0:
            visited[z - 1][x][y] = True
            box[z - 1][x][y] = t + 1
            queue.append((z - 1, x, y, t + 1))
        
        # down
        if is_down(z) and not visited[z + 1][x][y] and box[z + 1][x][y] == 0:
            visited[z + 1][x][y] = True
            box[z + 1][x][y] = t + 1
            queue.append((z + 1, x, y, t + 1))
        
        # same grid
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_range(nx, ny) and not visited[z][nx][ny] and box[z][nx][ny] == 0:
                visited[z][nx][ny] = True
                box[z][nx][ny] = t + 1  
                queue.append((z, nx, ny, t + 1))
        
        
m, n, h = map(int, input().split())
box = []
visited = []
for _ in range (h):
    tmp = [list(map(int, input().split())) for _ in range (n)]
    box.append(tmp)
    
    tmp2 = [[False for _ in range (m)] for _ in range (n)]
    visited.append(tmp2)

queue = deque()

for z in range (h):
    for x in range (n):
        for y in range (m):
            if box[z][x][y] == 1:
                queue.append((z, x, y, 0))
                box[z][x][y] = 0
                visited[z][x][y] = True

bfs()

ans = 0
vis = False
for z in range (h):
    for x in range (n):
        for y in range (m):
            ans = max(ans, box[z][x][y])
            if box[z][x][y] == 0 and not visited[z][x][y]:
                vis = True
                break
    
print(ans if not vis else -1)        
# for line in box:
#     for line2 in line:
#         print(line2)
# print()
# for line in visited:
#     for line2 in line:
#         print(line2)