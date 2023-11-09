n, x, y = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
x, y = x - 1, y - 1

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] # 우선순위: 상 하 좌 우

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n   

flag = True
while flag:
    print(grid[x][y], end=" ")
    move = False
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if is_range(nx, ny) and grid[x][y] < grid[nx][ny]:
            x, y = nx, ny
            move = True
            break
    if not move:
        break