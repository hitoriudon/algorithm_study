import sys
n = int(input())
x, y = map(int, input().split())
x, y = x - 1, y - 1

grid = [list(input()) for _ in range (n)]
visited = [[[False for _ in range (4)] for _ in range(n)] for _ in range(n)]
grid[x][y] = '@'
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0] # 동 북 서 남 (반시계)
dir, time = 0, 0
# print()
# for line in grid:
#     print(''.join(line))
    
def out_of_range(x, y, d): # while에서 항상 체크해야 함. True를 리턴했을 때는 그 즉시 종료할 수 있게끔.
    nx, ny = x + dxs[d], y + dys[d]
    return nx >= n or nx < 0 or ny >= n or ny < 0

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def visit(x, y, d):
    visited[x][y][d] = True
    
def move(x, y, d, t):
    nx, ny = x + dxs[d], y + dys[d]
    left, right = (d + 1) % 4, (d - 1) % 4
    if grid[nx][ny] == '#': # 진행 방향에 벽이 있으면
        return (x, y, left, t) # 현재 x, 현재 y, 반시계 방향으로 턴, 시간 그대로
    
    wall_x, wall_y = nx + dxs[right], ny + dys[right]
    
    if grid[wall_x][wall_y] == '#': # 진행 방향 기준 오른쪽에 벽이 있으면
        visit(x, y, d)
        visit(nx, ny, d)
        return (nx, ny, d, t + 1) # 한 칸 전진 x, 한 칸 전진 y, 방향 그대로, 시간 1초 증가
    
    elif grid[wall_x][wall_y] != '#': # 진행 방향 기준 오른쪽에 벽이 없으면
        visit(x, y, d)
        visit(nx, ny, d)
        nx, ny = nx + dxs[right], ny + dys[right] # 턴하고 바로 한 칸 전진해야 함
        visit(nx, ny, d)
        return (nx, ny, right, t + 2) # 두 칸 전진 x, 두 칸 전진 y, 시계 방향으로 턴, 시간 2초 증가

escape = False

while not escape:
    if visited[x][y][dir]:
        print(-1)
        sys.exit(0)
    if out_of_range(x, y, dir):
        escape = True
        break
    else:
        nx, ny, wx, wy, sx, sy, ex, ey = x + dxs[0], y + dys[0], x + dxs[1], y + dys[1], x + dxs[2], y + dys[2], x + dxs[3], y + dys[3]
        if is_range(nx, ny) and is_range(wx, wy) and is_range(sx, sy) and is_range(ex, ey):
            if grid[nx][ny] == grid[wx][wy] == grid[sx][sy] == grid[ex][ey] == '#':
                break

    if not out_of_range(x, y, dir) and not visited[x + dxs[dir]][y + dys[dir]][dir]:
        x, y, dir, time = move(x, y, dir, time)
        print(x, y, dir, time)
        continue

if escape:
    print(time + 1)
elif not escape:
    print(-1)
# for line in grid:
#     print(''.join(line))