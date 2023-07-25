from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range (n)]

visited = [[False for _ in range(m)] for _ in range(n)] # 주소값 유념

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque([(x, y, 1)])  #tuple. popleft() 한 번에 받으려고?
    visited[x][y] = True
    
    while queue:
        x, y, d = queue.popleft()
        if x == n - 1 and y == m - 1:
            print(d)
            break
        else:
            for i in range (4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, d+1))

print("정답 방식 visited")
print(visited)
bfs(0, 0)
# visited가 있으면 기존 그래프에 수를 추가하면 안 됨. 
# 그래서 마지막 인덱스일 때 브레이크를 걸어야 함.
# 내 visited 선언
# visited = [([False] * m)] * n                
# 주소값을 아예 생각을 안 했다.. 이러면 첫번째 배열 첫번째 인덱스에 True를 걸면 메모리가 복사된 거라 다 바뀌게 됨                   