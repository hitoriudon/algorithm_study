import sys
MIN = -sys.maxsize

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range (n)]
board = [[0 for _ in range (m)] for _ in range (n)] # 겹치는지 체크용

def draw(x1, y1, x2, y2):
    for i in range (x1, x2 + 1):
        for j in range (y1, y2 + 1):
            board[i][j] += 1 # 2가 있으면 겹치는 것

def clear_board():
    for i in range (n):
        for j in range (m):
            board[i][j] = 0

def check(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    for i in range (n):
        for j in range (m):
            if board[i][j] >= 2:
                return False # 겹친다
    return True # 안 겹친다

def add_two_square(x1, y1, x2, y2, x3, y3, x4, y4):
    first, second = 0, 0
    for i in range (x1, x2 + 1):
        for j in range (y1, y2 + 1):
            first += graph[i][j]
    for i in range (x3, x4 + 1):
        for j in range (y3, y4 + 1):
            second += graph[i][j]
    return first + second

def compare_two_square(x1, y1, x2, y2):
    max_sum = MIN
    
    for i in range (n):
        for j in range (m):
            for k in range (i, n):
                for l in range (j, m):
                    if check(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, add_two_square(x1, y1, x2, y2, i, j, k, l))
    
    return max_sum
    
# 첫번째 직사각형 잡기
max_sum = MIN
for i in range (n):
    for j in range (m):
        for k in range (i, n):
            for l in range (j, m):
                max_sum = max(max_sum, compare_two_square(i, j, k, l))
print(max_sum)