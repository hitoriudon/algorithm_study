from collections import deque

def check_in_grid(x, y, x1, y1, x2, y2): # args 모두 -1 해야함
    return x >= x1 and x <= x2 and y >= y1 and y <= y2

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def wind(x1, y1, x2, y2): # args 모두 -1 해야함
    boundary = deque()
    x, y, dir = x1, y1, 0 # starting point
    boundary.append(grid[x][y])
    
    while dir < 4:
        nx, ny = x + dxs[dir], y + dys[dir]
        if check_in_grid(nx, ny, x1, y1, x2, y2):
            boundary.append(grid[nx][ny])
            x, y = nx, ny
        else: # false
            dir += 1
    boundary.pop() # 처음 좌표가 두 번 넣어져서 그냥 팝
    boundary.rotate(1) # 시계 방향 회전
    
    x, y, dir, idx = x1, y1, 0, 1 # starting point
    grid[x][y] = boundary[0]
    while idx < len(boundary):
        nx, ny = x + dxs[dir], y + dys[dir]
        if check_in_grid(nx, ny, x1, y1, x2, y2):
            grid[nx][ny] = boundary[idx]
            x, y = nx, ny
            idx += 1
        else:
            dir += 1

def add(x1, y1, x2, y2):
    temp = []
    for _ in range (n):
        l = [0 for _ in range (m)]
        temp.append(l)
    
    for i in range (x1, x2 + 1):
        for j in range (y1, y2 + 1):
            total = grid[i][j]
            div = 1
            for dx, dy in zip(dxs, dys):
                if is_range(i + dx, j + dy):
                    total += grid[i + dx][j + dy]
                    div += 1
            temp[i][j] = total // div
    copy_array(temp, x1, y1, x2, y2)
    
def copy_array(copy_arr, x1, y1, x2, y2):
    for i in range (x1, x2 + 1):
        for j in range (y1, y2 + 1):
            grid[i][j] = copy_arr[i][j]

def Print():
    for l in grid:
        for i in l:
            print(i, end=" ")
        print()
        
# main
n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북

for _ in range (q):
    r1, c1, r2, c2 = map(int, input().split())
    wind(r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    add(r1 - 1, c1 - 1, r2 - 1, c2 - 1)

Print()