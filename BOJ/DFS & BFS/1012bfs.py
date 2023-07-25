from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = 2
    return 1

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

answer = []
for _ in range (t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range (m)] for _ in range (n)]
    visited = [[False for _ in range (m)] for _ in range (n)]
    
    for _ in range (k):
        loc1, loc2 = map(int, input().split())
        graph[loc2][loc1] = 1
        
    tmp = 0
    for i in range (n):
        for j in range (m):
            if not visited[i][j] and graph[i][j] == 1:
                tmp += bfs(i,j)
                
    answer.append(tmp)

for n in answer: print(n)