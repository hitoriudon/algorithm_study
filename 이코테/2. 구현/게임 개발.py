n, m = map(int, input().split())
x, y, dir = map(int, input().split())
board, visited = [], []
for _ in range (n):
    board.append(list(map(int, input().split())))
    visited.append([False] * m)

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] # 북 동 남 서

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

move = 0
while True:
    dir = (dir - 1) % 4 
    nx, ny = x + dxs[dir], y + dys[dir]
    
    if is_range(nx, ny) and board[nx][ny] == 0 and visited[nx][ny] == False: # 육지, 방문 안 함
        x, y = nx, ny
        move += 1
        visited[nx][ny] = True
        print(x, y)
        continue
    
    count = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and (board[nx][ny] == 1 or visited[nx][ny]) == True:
            count += 1
        
    if count == 4: # 백스텝
        new_dir = (dir + 2) % 4
        new_x, new_y = x + dxs[new_dir], y + dys[new_dir]
        
        if board[new_x][new_y] == 0:
            break
        else:
            x, y = new_x, new_y
print(move)