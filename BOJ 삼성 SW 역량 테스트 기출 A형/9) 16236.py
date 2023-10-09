from collections import deque

def find_starting_point():
    for i in range (n):
        for j in range (n):
            if grid[i][j] == 9:
                grid[i][j] = 0
                return i, j

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs():
    global level, eating, start_x, start_y
    
    distance = [[-1 for _ in range (n)] for _ in range (n)] # 안 갔다는 뜻
    queue = deque()
    queue.append((start_x, start_y, 0))
    distance[start_x][start_y] = 0
    dots = [] # 갈 수 있는 영역 다 보관하는 리스트
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    # 이동 가능한 곳 모두 dots에 넣기
    while queue:
        x, y, value = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and distance[nx][ny] == -1 and grid[nx][ny] <= level:
                distance[nx][ny] = value + 1
                queue.append((nx, ny, value + 1))
                dots.append((value + 1, nx, ny))

    # 먹기
    success = False
    for dist, x, y in sorted(dots):
        fish_level = grid[x][y]
        if fish_level >= 1 and level > fish_level:
            eating += 1
            grid[x][y] = 0
            start_x, start_y = x, y
            success = True
            return dist # (시간에 더해줘야 함)
    
    if not success:
        return 0 # 0이 인풋이면 끝났다고 알리게
    
n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]
start_x, start_y = find_starting_point()
level = 2
eating = 0
ans = 0

while True:
    if eating == level:
        level += 1
        eating = 0

    result = bfs()
    
    if result != 0:
        ans += result
    elif result == 0:
        break

print(ans)