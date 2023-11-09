from collections import deque

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs(value):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and value > grid[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                candidate.append((grid[nx][ny], (-1) * nx, (-1) * ny)) # 우선 순위 고려. sort reverse한 다음 맨 앞에 거 택할 거라서
                
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1 # 인덱스 보정

for i in range (k):
    queue = deque()
    visited = [[False for _ in range (n)] for _ in range (n)]
    visited[r][c] = True
    queue.append((r, c))
    
    candidate = []

    bfs(grid[r][c])
    if len(candidate) == 0:
        break
    select = sorted(candidate, reverse= True)[0]
    r, c = (-1) * select[1], (-1) * select[2]

print(r + 1, c + 1) # 정답을 위한 인덱스 보정