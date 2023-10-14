from copy import deepcopy

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def out_range(x, y):
    return not (x >= 0 and x < n and y >= 0 and y < n)

def make_road():
    visited = [[False for _ in range (n)] for _ in range (n)]
    x, y = 0, 0
    visited[x][y] = True
    dir = 0
    loc = [(x, y, dir)]
    while not (x == n // 2 and y == n // 2):
        nx, ny = x + dxs[dir], y + dys[dir]
        if in_range(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            loc.append((nx, ny, dir))
            x, y = nx, ny
        else:
            dir = (dir + 1) % 4

    temp = deepcopy(loc)
    temp.reverse()
    temp.pop()
    loc.pop()
    for i in range (len(temp)):
        dir = (temp[i][2] + 2) % 4 
        temp[i] = (temp[i][0], temp[i][1], dir)
    road = temp + loc
    
    return road

n, m, h, k = map(int, input().split())

# 도망자들 세팅
avs = [] 
for _ in range (m):
    r, c, avoid_type = map(int, input().split())
    if avoid_type == 1:
        avs.append([r - 1, c - 1, 1]) # 1하고 3으로만 dxs, dys 움직이면 됨 (동, 서)
    else:
        avs.append([r - 1, c - 1, 0]) # 2하고 0으로만 dxs, dys 움직이면 됨 (남, 북)

# 트리 세팅
tree = [[False for _ in range (n)] for _ in range (n)]
for _ in range (h):
    r, c = map(int, input().split())
    tree[r-1][c-1] = True # 여긴 트리가 있어요

# 도망자는 이 길과 이 방향으로만 간다. 각각 nx, ny, 바라보는 방향
catch_road = make_road()
ans = 0

# k번 라운드를 진행한다
for turn in range (k):
    cx, cy, cdir = catch_road[turn % len(catch_road)] # catcher의 현재 좌표, 바라보는 방향
    
    # 도망자는 먼저 이동을 한다
    # 술래와의 거리가 최단 거리가 3 이하인 애만 이동 가능하다
    for i in range (len(avs)):
        ax, ay, a_dir = avs[i] # avoider의 현재 좌표, 이동 타입(좌우 or 하상)
        
        if abs(cx - ax) + abs(cy - ay) <= 3:
            a_nx, a_ny = ax + dxs[a_dir], ay + dys[a_dir]
            
            if out_range(a_nx, a_ny): # 나갔으면 턴하고 다시 전진
                a_dir = (a_dir + 2) % 4
                a_nx, a_ny = ax + dxs[a_dir], ay + dys[a_dir]
                
            if in_range(a_nx, a_ny) and (a_nx != cx or a_ny != cy): # 술래도 없고 격자 안에 있으면
                avs[i] = [a_nx, a_ny, a_dir] 
            else:
                avs[i] = [ax, ay, a_dir]
    
    # 그리드에 도망자 현황 최신화
    grid = [[0 for _ in range (n)] for _ in range (n)]
    for i in range (len(avs)):
        x, y = avs[i][0], avs[i][1]
        grid[x][y] += 1
    
    # 술래는 turn + 1만큼 이동을 한다
    cx, cy, cdir = catch_road[(turn + 1) % len(catch_road)]
    
    # 잡는다. 트리가 있으면 잡지 않는다. 잡으면 점수를 올린다.
    remove_list = []
    for i in range (3):
        n_cx, n_cy = cx + dxs[cdir] * i, cy + dys[cdir] * i
        if in_range(n_cx, n_cy) and grid[n_cx][n_cy] >= 1 and not tree[n_cx][n_cy]:
            ans += (turn + 1) * grid[n_cx][n_cy]
            remove_list.append((n_cx, n_cy))
    
    # 걸러준다. 시간 복잡도 안 걸리려나...
    copy_avs = []
    for i in range (len(avs)):
        a_x, a_y, a_way = avs[i]
        cnt = 0
        for j in range (len(remove_list)):
            tx, ty = remove_list[j]
            if not (a_x == tx and a_y == ty): # 찾았다 지울 인덱스
                cnt += 1
        if cnt == len(remove_list):
            copy_avs.append(avs[i])

    avs = deepcopy(copy_avs)
    
print(ans)

# 정답: 309
# 5 24 20 82
# 4 5 2
# 2 1 1
# 1 4 2
# 2 5 1
# 1 1 1
# 1 3 1
# 5 3 1
# 3 1 2
# 3 5 2
# 4 4 2
# 4 3 2
# 2 2 2
# 3 2 2
# 1 2 2
# 1 5 1
# 5 1 1
# 4 1 2
# 2 3 2
# 2 4 1
# 5 4 1
# 5 2 2
# 4 2 2
# 3 4 1
# 5 5 1
# 3 2
# 3 5
# 2 2
# 4 2
# 3 3
# 5 4
# 3 4
# 5 5
# 2 4
# 2 3
# 1 1
# 2 5
# 5 1
# 1 2
# 5 3
# 4 4
# 2 1
# 4 5
# 1 4
# 4 3
