# 14502, 연구소, G4, pypy3
from collections import deque
import copy

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs():
    board = copy.deepcopy(graph)
    queue = deque(virus)
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_range(nx, ny) and board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx, ny))
            
    global answer
    
    tmp = 0
    for i in range (n):
        tmp += board[i].count(0)
    
    answer = max(answer, tmp)
    
def setWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range (n):
        for j in range (m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                setWall(cnt+1)
                graph[i][j] = 0 # 다시 벽 허물기

n, m = map(int, input().split())
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서

graph = [list(map(int, input().split())) for _ in range (n)]
answer = 0
virus = []
for i in range (n):
    for j in range (m):
        if graph[i][j] == 2:
            virus.append((i, j))
            
setWall(0)
print(answer)