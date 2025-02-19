from collections import deque
def is_range(x, y):
    return x >= -1 and y >= 0 and x < r and y < c

def is_range2(x, y):
    return x >= 0 and y >= 0 and x < r and y < c

def first_move(x, y): # 정령의 좌표
    # 비어있나 체크
    indexes = [(1, -1), (2, 0), (1, 1)]
    
    for dx, dy in indexes:
        nx, ny = x + dx, y + dy
        
        if not is_range(nx, ny) or grid[nx][ny] != 0:
            return (-1, -1)
    
    return (x + 1, y)

def first_move2(x, y):
    nx, ny = x + 1, y

    if grid[nx][ny] != 0:
        return (-1, -1)
    return (x, y)

def second_move(x, y): # 왼쪽이고, 정령 좌표 리턴 받은 다음 메인에서 d-1 % 처리 해줘야함
    indexes = [(-1, -1), (0, -2), (1, -2), (1, -1), (2, -1)]
    
    for dx, dy in indexes:
        nx, ny = x + dx, y + dy
        
        if not is_range(nx, ny) or grid[nx][ny] != 0:
            return (-1, -1)
    
    return (x + 1, y - 1)

def second_move2(x, y): # 왼쪽이고, 정령 좌표 리턴 받은 다음 메인에서 d-1 % 처리 해줘야함
    #indexes = [(-1, -1), (0, -2), (1, -2), (1, -1), (2, -1)]
    indexes = [(1, -2), (1, -1), (2, -1)]
    
    for dx, dy in indexes:
        nx, ny = x + dx, y + dy
        
        if not is_range(nx, ny) or grid[nx][ny] != 0:
            return (-1, -1)
    
    return (x + 1, y - 1)

def third_move(x, y): # 오른쪽이고, 정령 좌표 리턴 받은 다음 메인에서 d+1 % 처리 해줘야함
    indexes = [(-1, 1), (0, 2), (1, 2), (1, 1), (2, 1)]

    for dx, dy in indexes:
        nx, ny = x + dx, y + dy
        
        if not is_range(nx, ny) or grid[nx][ny] != 0:
            return (-1, -1)
    
    return (x + 1, y + 1)

def third_move2(x, y): # 오른쪽이고, 정령 좌표 리턴 받은 다음 메인에서 d+1 % 처리 해줘야함
    #indexes = [(-1, 1), (0, 2), (1, 2), (1, 1), (2, 1)]
    indexes = [(1, 2), (1, 1), (2, 1)]
    for dx, dy in indexes:
        nx, ny = x + dx, y + dy
        
        if not is_range(nx, ny) or grid[nx][ny] != 0:
            return (-1, -1)
    
    return (x + 1, y + 1)

def bfs(sx, sy):
    can_approach_wizard_idxex = [(sx, sy)]
    vis = [[False for _ in range (c)] for _ in range (r)]
    que = deque()
    que.append((sx, sy))
    #print("before", can_approach_wizard_idxex, sx, sy)

    while que:
        x, y = que.popleft()
        tx, ty = -1, -1
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if is_range2(nx, ny):
                vis[nx][ny] = True
                
                if grid[nx][ny] == 2:
                    # 상하좌우에 인접한 1이 있는가?
                    tx, ty = nx, ny

        tmp_idxes = []
        if (tx, ty) != (-1, -1):
            # 출구에 인접한 블록들 다 우선 넣어놓기
            for dx, dy in dir:
                nx, ny = tx + dx, ty + dy
                if is_range2(nx, ny) and not vis[nx][ny] and grid[nx][ny] >= 1:
                    tmp_idxes.append((nx, ny))
            
            # 출구에 인접한 블록들의 주인(정령) 찾기
            for x, y in tmp_idxes:
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if is_range2(nx, ny) and not vis[nx][ny] and grid[nx][ny] == 3:
                        que.append((nx, ny))
                        vis[nx][ny] = True
                        can_approach_wizard_idxex.append((nx, ny))
    #print("after", can_approach_wizard_idxex)
    ans_index = sorted(can_approach_wizard_idxex, reverse=True)[0]
    return ans_index[0]
            
# main
r, c, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range (k)]
grid = [[0 for _ in range (c)] for _ in range (r)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0

for i in range (k):
    x, y, d = -1, info[i][0] - 1, info[i][1] # start row idx, start column idx, dir
    first_flag = True

    while True:
        if first_flag:
            rx, ry = first_move2(x, y)
            if (rx, ry) == (-1, -1):
                break
            x, y = rx, ry
            first_flag = False
            continue
        else:
            rx, ry = first_move(x, y)
            if (rx, ry) != (-1, -1):
                x, y = rx, ry
                continue

        if x <= 0:
            rx, ry = second_move2(x, y)
            if (rx, ry) != (-1, -1):
                x, y, d = rx, ry, (d-1) % 4
                continue
            rx, ry = third_move2(x, y)
            if (rx, ry) != (-1, -1):
                x, y, d = rx, ry, (d+1) % 4
                continue
            break
        elif x > 0:
            rx, ry = second_move(x, y)
            if (rx, ry) != (-1, -1):
                x, y, d = rx, ry, (d-1) % 4
                continue
            rx, ry = third_move(x, y)
            if (rx, ry) != (-1, -1):
                x, y, d = rx, ry, (d+1) % 4
                continue
            break
    if x <= 0:
        grid = [[0 for _ in range (c)] for _ in range (r)]
        continue
    
    grid[x][y] = 3 # 정령
    for j in range (4):
        dx, dy = dir[j]
        if j == d:
            grid[x + dx][y + dy] = 2
        else:
            grid[x + dx][y + dy] = 1
    ret = bfs(x, y) + 2
    # for line in grid:
    #     print(line)
    ans += ret

print(ans)
        
# 6 6 5
# 2 2
# 5 0
# 5 3
# 4 1
# 2 1