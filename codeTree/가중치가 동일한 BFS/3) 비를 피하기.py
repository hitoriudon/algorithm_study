from collections import deque

def find_people_location():
    temp = []
    for i in range (size):
        for j in range (size):
            if grid[i][j] == 2:
                temp.append((i, j))
    return temp

def is_range(x, y):
    return x >= 0 and x < size and y >= 0 and y < size

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        x, y, value = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 1:
                visited[nx][ny] = True # 방문 처리는 우선 해야함
                
                if grid[nx][ny] != 3: # 도착하지 않았다면
                    queue.append((nx, ny, value + 1))
                
                elif grid[nx][ny] == 3: # 비를 피할 수 있는 곳에 도착했다면
                    return value + 1 # 현재 distance 리턴 
    
    return -1 # 덱이 비었는데도 리턴이 안 됐으면 -1

size, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (size)]
people = find_people_location()

ans = [[0 for _ in range (size)] for _ in range (size)]

# 한 명씩 하는 BFS
for person in people:
    x, y = person
    
    queue = deque([(x, y, 0)])
    visited = [[False for _ in range (size)] for _ in range (size)]
    visited[x][y] = True
    
    ans[x][y] = bfs()

# 정답 출력
for line in ans:
    for num in line:
        print(num, end=" ")
    print()