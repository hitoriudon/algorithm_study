from collections import deque
# import time as t

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs():
    while queue:
        x, y, sx, sy = queue.popleft()
        
        if x == ex and y == ey:
            lock[sx][sy] = True # 잠궈
            return [sx, sy]
            
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, sx, sy))
                

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
store = []
for i in range (m):
    r, c = map(int, input().split())
    store.append((r - 1, c - 1)) # 인덱스 보정
# store.sort() # 행 작은 거부터, 그러면 열 작은 거부터.

lock = [[False for _ in range (n)] for _ in range (n)] # 이미 선택이 된 베이스캠프나 편의점이라면 True값을 가진다.
    
dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0] # 북 서 동 남

time = 0
people = []
while True:
    for i in range (len(people)):
        
        # 이미 이동을 완료한 사람이라면 스킵하도록
        if people[i][0] == -1 and people[i][1] == -1:
            continue
        
        # 이동 시작
        sx, sy = people[i][0], people[i][1]
        back_x = [[0 for _ in range (n)] for _ in range (n)]
        back_y = [[0 for _ in range (n)] for _ in range (n)]
        
        que = deque()
        que.append((sx, sy, 0))
        vis = [[False for _ in range (n)] for _ in range (n)]
        vis[sx][sy] = True
        
        store_x, store_y = store[i]
        
        # bfs 탐색
        while que:
            x, y, move = que.popleft()
            
            if x == store_x and y == store_y:
                
                while not (x == sx and y == sy):
                    bx, by = back_x[x][y], back_y[x][y]
                    if bx == sx and by == sy:
                        break
                    x, y = bx, by
                sx, sy = x, y # 이동
                break
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if is_range(nx, ny) and not lock[nx][ny] and not vis[nx][ny]:
                    
                    vis[nx][ny] = True
                    que.append((nx, ny, move + 1))
                    back_x[nx][ny] = x
                    back_y[nx][ny] = y
                    
        # 편의점 락
        # 만약 도착했으면, lock 트루하고 그 사람 이동하게 만들면 안 됨
        if sx == store_x and sy == store_y:
            lock[store_x][store_y] = True
            people[i][0], people[i][1] = -1, -1 # 할 수 없게 만들어
        else:
            people[i][0], people[i][1] = sx, sy
        # print(time)
        # for line in lock:
        #     print(line)
    # t.sleep(5)
    
    if 1 <= time <= m: 
        ex, ey = store[time - 1] 
        
        # 베이스 캠프 찾기
        basecamp = []
        for i in range (n):
            for j in range (n):
                if grid[i][j] == 1 and not lock[i][j]:
                    basecamp.append((i, j, i, j)) # 스타트 인덱스를 같이 가지고 있는다.
        
        # 베이스캠프를 찾는 bfs를 진행한다.
        queue = deque(basecamp)
        visited = [[False for _ in range (n)] for _ in range (n)]
        for q in queue:
            visited[q[0]][q[1]] = True # 먼저 방문 처리
            
        for i in range (n):
            for j in range (n):
                visited[i][j] = lock[i][j]
        
        # 사람이 있어야 할 곳을 리턴한다
        person_location = bfs()
        
        temp_X, temp_Y = person_location[0], person_location[1]
        lock[temp_X][temp_Y] = True
        people.append(person_location)
    
    # 이동할 수 없는 사람 세기
    cnt = 0
    for i in range (len(people)):
        if people[i][0] == -1 and people[i][1] == -1:
            cnt += 1
    if len(people) != 0 and cnt == len(people):
        print(time)
        exit(0)
    
    time += 1
    
# 5 3
# 0 0 0 0 0
# 1 0 0 0 1
# 0 0 0 0 0
# 0 1 0 0 0
# 0 0 0 0 1
# 2 3
# 4 4
# 5 1

# 시간 초과
# 2 1
# 1 1
# 0 0
# 2 2

# 답: 7
# 4 5
# 1 0 1 1
# 1 0 1 1
# 0 0 0 1
# 1 0 1 1
# 4 2
# 3 1
# 3 3
# 3 2
# 1 2