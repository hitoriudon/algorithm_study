from collections import deque
import sys
INT_MAX = sys.maxsize

n = int(input())
grid = [list(input()) for _ in range (n)]

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

answer = INT_MAX
# 최소 세 개의 동전을 줍는 백트래킹
def f(level, begin):
    global answer
    if level == number_of_coins:
        if len(arr) >= 3:
            
            # 동전 줍기 bfs
            queue = deque()
            queue.append((0, sx, sy))
            for not_use, tx, ty in arr:
                visited = [[False for _ in range (n)] for _ in range (n)]
                # 동전 먼저 줍기 bfs
                while queue:
                    v, x, y = queue.popleft()
                    if x == tx and y == ty:
                        queue = deque()
                        queue.append((v, tx, ty))
                        break
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x + dx, y + dy
                        if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != '#':
                            visited[nx][ny] = True
                            queue.append((v + 1, nx, ny))
            
            # 마지막 동전 주운 지점부터 bfs 시작
            visited = [[False for _ in range (n)] for _ in range (n)]
            
            while queue:
                dist, x, y = queue.popleft()    
                if x == ex and y == ey:
                    answer = min(answer, dist)
                    return

                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != '#':
                        visited[nx][ny] = True
                        queue.append((dist + 1, nx, ny))
        return
    
    arr.append(coins[begin])
    f(level + 1, begin + 1)
    arr.pop()
    
    f(level + 1, begin + 1)    
    
# 그리드에 있는 동전 찾기, 시작점 찾기, 도착점 찾기
coins = []
number_of_coins = 0
sx, sy, ex, ey = 0, 0, 0, 0
for i in range (n):
    for j in range (n):
        select = grid[i][j]
        if '1' <= select <= '9':
            coins.append((int(select), i, j)) # 동전이 있는 위치를 넣어놓기
            number_of_coins += 1
        elif select == 'S':
            sx, sy = i, j
        elif select == 'E':
            ex, ey = i, j

coins.sort()

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
arr = []

f(0,0)
print(answer if answer != INT_MAX else -1)