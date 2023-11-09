from copy import deepcopy
def find_bombs(arr):
    temp = []
    for i in range (n):
        for j in range (n):
            if arr[i][j] == 1:
                temp.append((i, j))
    return temp

def f(cnt):
    global bombs, answer
    if cnt == bombs:
        temp = deepcopy(grid)
        answer = max(answer, boom(temp))
        return

    for i in range (3):
        arr.append(i)
        f(cnt + 1)
        arr.pop()
        
def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def boom(board):
    idx = 0
    # 우선 다 초토화
    for x, y in location:
        board[x][y] = -1 # 시작 지점 초토화
        choice = arr[idx]
        idx += 1
        for dx, dy in KIND[choice]:
            nx, ny = x + dx, y + dy
            if is_range(nx, ny):
                board[nx][ny] = -1 # 초토화
    # 카운트
    eli = 0
    for line in board:
        eli += line.count(-1)
    
    return eli
            
n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]
location = find_bombs(grid)
bombs = len(location)
KIND = [
    [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    [(-1, 0), (1, 0), (0, -1), (0, 1)],
    [(-1, 1), (-1, -1), (1, -1), (1, 1)]
]
arr = []
answer = 0
f(0)
print(answer)