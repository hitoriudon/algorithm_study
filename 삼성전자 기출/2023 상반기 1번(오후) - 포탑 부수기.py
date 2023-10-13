from collections import deque
import time
def can_quit():
    cnt = 0
    for i in range (n):
        for j in range (m):
            if grid[i][j] != 0:
                cnt += 1
    return cnt <= 1 # if can_quit(): break

def find_min(): # 공격력 최솟값 찾기
    temp = 5001 # 공격력이 최대 5000이라서
    for i in range (n):
        for j in range (m):
            if grid[i][j] != 0:
                temp = min(temp, grid[i][j])
    return temp

def find_max(): # 공격력 최댓값 찾기
    temp = 0
    for i in range (n):
        for j in range (m):
            if grid[i][j] != 0 and not(i == sx and j == sy):
                temp = max(temp, grid[i][j])
    
    return temp

def find_attacker(candidate):
    # 1) 최근에 공격한 경험이 있는지
    recent_list = [recent[i][j] for i, j in candidate]
    min_recent = min(recent_list) 
    
    for idx in range (len(candidate)):
        i, j = candidate[idx]
        if recent[i][j] != min_recent:
            candidate[idx] = (-1, -1) # 볼 필요 없다
    # 2) 인덱스 합이 가장 큰 포탑으로
    max_list = [i + j for i, j in candidate]
    max_idx = max(max_list)
    for idx in range (len(candidate)):
        i, j = candidate[idx]
        if i + j != max_idx:
            candidate[idx] = (-1, -1)
    # 3) y가 가장 큰 포탑으로
    candidate = sorted(candidate, key=lambda x : x[1], reverse= True)

    return candidate[0]

def find_attacked(candidate):
    # 1) 가장 공격한지 오래 된 포탑으로
    recent_list = [recent[i][j] for i, j in candidate]
    max_recent = max(recent_list)
    
    for idx in range (len(candidate)):
        i, j = candidate[idx]
        if recent[i][j] != max_recent:
            candidate[idx] = (n+1, m+1) # 볼 필요 없다
    # 2) 인덱스 합이 가장 작은 포탑으로
    min_list = [i + j for i, j in candidate]
    min_idx = min(min_list)
    for idx in range (len(candidate)):
        i, j = candidate[idx]
        if i + j != min_idx:
            candidate[idx] = (n+1, m+1)
    # 3) y가 가장 작은 포탑으로
    candidate = sorted(candidate, key=lambda x : x[1])
    
    return candidate[0]    

def out_of_range(x, y):
    if x < 0: return (n-1, y)
    elif x >= n: return (0, y)
    elif y < 0: return (x, m-1)
    elif y >= m: return (x, 0)
    return False

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def lazer():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
    
    while queue:
        x, y = queue.popleft()

        if x == tx and y == ty:
            return True
        for dx, dy in zip(dxs, dys):
            for dx, dy in zip(dxs, dys):
                nx = (x + dx + n) % n
                ny = (y + dy + m) % m

                # 이미 방문한 포탑이라면 넘어갑니다.
                if visited[nx][ny]: 
                    continue

                # 벽이라면 넘어갑니다.
                if grid[nx][ny] == 0: 
                    continue

                visited[nx][ny] = True
                back_x[nx][ny] = x
                back_y[nx][ny] = y
                queue.append((nx, ny))
            # nx, ny = x + dx, y + dy
            # if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 0:
            #     queue.append((nx, ny))
            #     visited[nx][ny] = True
            #     back_x[nx][ny] = x
            #     back_y[nx][ny] = y
            # elif out_of_range(nx, ny):
            #     nx, ny = out_of_range(nx, ny)
            #     if not visited[nx][ny] and grid[nx][ny] != 0:
            #         queue.append((nx, ny))
            #         visited[nx][ny] = True
            #         back_x[nx][ny] = x
            #         back_y[nx][ny] = y
        # for line in back_x:
        #     print(line)
        # for line in back_y:
        #     print(line)
        # print()
    return False 

def boom(x, y):
    dxs2, dys2 = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    
    for dx2, dy2 in zip(dxs2, dys2):
        nx = (tx + dx2 + n) % n
        ny = (ty + dy2 + m) % m

        # 각성한 포탑 자기 자신일 경우 넘어갑니다.
        if nx == sx and ny == sy: 
            continue

        # 가장 강한 포탑일 경우 pow만큼의 공격을 진행합니다.
        if nx == tx and ny == ty:
            grid[nx][ny] -= grid[sx][sy]
            if grid[nx][ny] < 0: 
                grid[nx][ny] = 0
            is_active[nx][ny] = True
        # 그 외의 경우 pow // 2만큼의 공격을 진행합니다.
        else:
            grid[nx][ny] -= grid[sx][sy] // 2
            if grid[nx][ny] < 0: 
                grid[nx][ny] = 0
            is_active[nx][ny] = True
    # for line in is_active:
    #     print(line)
                    
n, m, k = map(int, input().split())
path = [[0 for _ in range (m)] for _ in range (n)]
grid = [list(map(int, input().split())) for _ in range (n)]
recent = [[0 for _ in range (m)] for _ in range (n)]
back_x = [[0 for _ in range (m)] for _ in range (n)]
back_y = [[0 for _ in range (m)] for _ in range (n)]

for turn in range (k):
    # 공격자 포탑 정하기
    attack_tower_candidate = []
    min_attack = find_min()
    for i in range (n):
        for j in range (m):
            if grid[i][j] == min_attack:
                attack_tower_candidate.append((i, j))

    sx, sy = find_attacker(attack_tower_candidate) # start x, y
    grid[sx][sy] += n + m # 공격력 증가
    
    
    recent[sx][sy] = 0 # 공격자가 됐으니까 초기화
    # 공격자 아닌 애들 recent += 1
    for i in range (n):
        for j in range (m):
            if not (i == sx and j == sy):
                recent[i][j] += 1
    # for line in recent:
    #     print(line)
        
    # 피공격자 포탑 정하기
    attacked_tower_candidate = []
    max_attack = find_max()
    for i in range (n):
        for j in range (m):
            if grid[i][j] == max_attack:
                attacked_tower_candidate.append((i, j))
    
    tx, ty = find_attacked(attacked_tower_candidate) # target x, y
    
    # 레이저 공격
    queue = deque()
    visited = [[False for _ in range (m)] for _ in range (n)] # k에 대한 for 문 안에서
    queue.append((sx, sy))
    visited[sx][sy] = True
    
    can_attack = lazer()
    
    is_active = [
        [False] * m
        for _ in range(n)
    ]
    
    
    if can_attack:
        is_active[sx][sy] = True
        grid[tx][ty] -= grid[sx][sy]
        if grid[tx][ty] < 0: 
            grid[tx][ty] = 0
        is_active[tx][ty] = True
        # 기존의 경로를 역추적하며
        # 경로 상에 있는 모든 포탑에게 power // 2만큼의 공격을 진행합니다.
        cx = back_x[tx][ty]
        cy = back_y[tx][ty]

        while not (cx == sx and cy == sy):
            
            grid[cx][cy] -= grid[sx][sy] // 2
            if grid[cx][cy] < 0: 
                grid[cx][cy] = 0
            is_active[cx][cy] = True
            
            next_cx = back_x[cx][cy]
            next_cy = back_y[cx][cy]
            cx = next_cx
            cy = next_cy
    # 폭탄
    else:
        grid[tx][ty] -= grid[sx][sy]
        if grid[tx][ty] < 0:
            grid[tx][ty] = 0
        is_active[tx][ty] = True
        is_active[sx][sy] = True
    
        boom(tx, ty)
    
    if can_quit():
        break # 그 즉시 종료
    
    # 수리하기
    for i in range (n):
        for j in range (m):
            if not is_active[i][j] and grid[i][j] != 0:
                grid[i][j] += 1
                
    
    # print()
    # for line in grid:
    #     for num in line:
    #         print(num, end=" ")
    #     print()

ans = 0
for i in range (n):
    for j in range (m):
        ans = max(ans, grid[i][j])
print(ans)
