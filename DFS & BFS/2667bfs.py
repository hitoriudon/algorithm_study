from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    answer.append(cnt)
    
n = int(input())
graph = [list(map(int, input())) for _ in range (n)]
visited = [[False for _ in range (n)] for _ in range (n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

for i in range (n):
    for j in range (n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i,j)

print(len(answer))
for n in sorted(answer):
    print(n)