from collections import deque

def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def bfs():
    que = deque()
    result = [[float('Inf') for _ in range (n)] for _ in range (n)]
    que.append((0, 0))
    result[0][0] = 0 # memoization bfs
    
    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
    
    while que:
        x, y = que.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_range(nx, ny) and result[x][y] + road[nx][ny] < result[nx][ny]:
                result[nx][ny] = result[x][y] + road[nx][ny]
                que.append((nx, ny))
    
    return result[n-1][n-1]

# main
T = int(input())
for t in range (1, T+1):
    n = int(input())
    road = []
    for _ in range (n):
        param = input()
        temp = []
        for c in param:
            temp.append(int(c))
        road.append(temp)
    
    ret = bfs()
    
    print("#" + str(t) + " " + str(ret))
    