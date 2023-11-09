from collections import deque

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

ans = 0
def bfs(dots):
    global ans
    
    queue = deque(dots)
    visited = [[False for _ in range (n)] for _ in range (n)]
    for x, y in queue:
        visited[x][y] = True
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
    
    # 갈 수 있는 도시 체크
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and u <= abs(grid[x][y] - grid[nx][ny]) <= d:
                visited[nx][ny] = True
                queue.append((nx, ny))
     
    # 개수 체크
    can_visit = 0
    for line in visited:
        can_visit += line.count(True)
    
    ans = max(ans, can_visit)
        
def find_combination(level, begin):
    if level == k:
        bfs(selected_dots)
        return
    
    for i in range (begin, len(dot_list)):
        selected_dots[level] = dot_list[i]
        find_combination(level + 1, i + 1)

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]

selected_dots = [(0, 0) for _ in range (k)]

# 조합(백트래킹)을 위한 일차원 배열로 만들기...
dot_list = []
for i in range (n):
    for j in range (n):
        dot_list.append((i, j))

find_combination(0, 0)

print(ans)