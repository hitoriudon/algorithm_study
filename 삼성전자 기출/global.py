t = 6
testcase = []
for _ in range (t):
    i_n, i_sx, i_sy, i_ex, i_ey = map(int, input().split())
    testcase.append((i_n, i_sx, i_sy, i_ex, i_ey))

from collections import deque
def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while queue:
        x, y = queue.popleft()
        
        if x == ex and y == ey:
            board[ex][ey] = 1 # 끝점 보드에 칠해주기
            tx = back_x[x][y]
            ty = back_y[x][y]
            while not (tx == sx and ty == sy):
                board[tx][ty] = 1
                next_tx = back_x[tx][ty]
                next_ty = back_y[tx][ty]
                tx = next_tx
                ty = next_ty
            board[tx][ty] = 1 # 시작점 보드에 칠해주기
            return True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not vis[nx][ny] and grid[nx][ny] == 0:
                vis[nx][ny] = True
                queue.append((nx, ny))
                back_x[nx][ny] = x
                back_y[nx][ny] = y
    return False
# main
for test in range (t):
    grid = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    grid[3][2] = test % 2
    n, sx, sy, ex, ey = testcase[test]
    board = [[0 for _ in range (n)] for _ in range (n)]
    vis = [[False for _ in range (n)] for _ in range (n)]
    
    queue = deque()
    queue.append((sx, sy))
    vis[sx][sy] = True
    back_x = [[0 for _ in range (n)] for _ in range (n)]
    back_y = [[0 for _ in range (n)] for _ in range (n)]

    result = bfs()
    for line in board:
        print(line)
    print(result)
# 4 0 0 3 3
# 4 1 1 3 3
# 4 1 1 3 0
# 4 0 3 0 0
# 4 0 2 2 3
# 4 0 2 2 3