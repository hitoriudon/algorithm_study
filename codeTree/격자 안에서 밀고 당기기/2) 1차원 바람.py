from collections import deque

# deque rotate() 기능
def shift(r, dir):
    grid[r].rotate(dir)
    
# 행 기준 upside (index 더 작은 쪽으로)
def spread_up(r, dir): # 바람 시작 row, m 크기, rotate 방향
    for i in range (r, 0, -1):
        flag = False
        for j in range (m):
            if grid[i][j] == grid[i-1][j]:
                flag = True
        if flag:
            dir = dir * (-1)
            shift(i - 1, dir)
        elif flag == False:
            return

# 행 기준 downside (index 더 큰 쪽으로)        
def spread_down(r, dir): # 바람 시작 row, m 크기, rotate 방향
    for i in range (r, n - 1):
        flag = False
        for j in range (m):
            if grid[i][j] == grid[i+1][j]:
                flag = True
        if flag:
            dir = dir * (-1)
            shift(i + 1, dir)
        elif flag == False:
            return

# 2차원 배열 출력
def Print():
    for g in grid:
        for num in g:
            print(num, end=" ")
        print()
    print()
    
# main
n, m, q = map(int, input().split())
grid = [deque(map(int, input().split())) for _ in range (n)] # deque를 사용하면 temp를 이용한 shift 불필요

direction = {'L': 1, 'R': -1} # 왼쪽인 경우엔 rotate(1), 오른쪽인 경우엔 rotate(-1)이라서.
Q = []
for _ in range (q):
    row, dir = map(str, input().split())
    Q.append((int(row) - 1, direction[dir])) # row index, 1 or -1

for i in range (q):
    start_row, wind = Q[i]
    
    shift(start_row, wind)
    spread_up(start_row, wind)    
    spread_down(start_row, wind)
    
Print()