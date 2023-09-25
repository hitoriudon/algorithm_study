# 14499, 주사위 굴리기, G4

#   B
# D A C 
#   E
#   F
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0 

def right(a, b, c, d, e, f):
    a, b, c, d, e, f = d, b, a, f, e, c
    return (a, b, c, d, e, f)

def left(a, b, c, d, e, f):
    a, b, c, d, e, f = c, b, f, a, e, d
    return (a, b, c, d, e, f)

def up(a, b, c, d, e, f):
    a, b, c, d, e, f = e, a, c, d, f, b    
    return (a, b, c, d, e, f)

def down(a, b, c, d, e, f):
    a, b, c, d, e, f = b, f, c, d, a, e
    return (a, b, c, d, e, f)

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
commands = list(map(int, input().split()))

dir = {1: right, 2: left, 3: up, 4: down}
dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0] # 동 서 북 남

for command in commands:
    nx, ny = x + dxs[command - 1], y + dys[command - 1] # 주사위 이동 좌표
     
    if is_range(nx, ny):
        a, b, c, d, e, f = dir[command](a, b, c, d, e, f) # 주사위 이동
        
        if grid[nx][ny] == 0:
            grid[nx][ny] = f
        
        elif grid[nx][ny] != 0:
            f = grid[nx][ny]
            grid[nx][ny] = 0
        x, y = nx, ny
        print(a)