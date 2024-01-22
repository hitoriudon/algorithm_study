# 2072, 오목, S3
n = int(input())

put = [list(map(int, input().split())) for _ in range (n)]
        
board = [[-1 for _ in range (19)] for _ in range (19)]

for i in range (n):
    x, y = put[i][0] - 1, put[i][1] - 1
    
    color = 0 # 0: black, 1: white
    if i % 2 == 1: # white
        color = 1
    
    board[x][y] = color
    
    # 가로 체크
    start_y = y - 4
    end_y = y + 5
    
    if start_y < 0:
        start_y = 0
    if end_y > 18:
        end_y = 19
    
    black, white = 0, 0
    for y in range (start_y, end_y):
        if board[x][y] == 0:
            black += 1
            white = 0
        elif board[x][y] == 1:
            white += 1
            black = 0
        elif board[x][y] == -1:
            white, black = 0, 0
    
    # 세로 체크
    start_x = x - 4
    end_x = x + 5
    
    if start_x < 0:
        start_x = 0
    if end_x > 18:
        end_x = 19
    
    black, white = 0, 0
    for x in range (start_x, end_x):
        if board[x][y] == 0:
            black += 1
            white = 0
        elif board[x][y] == 1:
            white += 1
            black = 0
        elif board[x][y] == -1:
            white, black = 0, 0
        
        if black == 5 or white == 5:
            print(i + 1)
            exit(0)
    
    # 대각선 (\) 체크
    x, y = put[i][0] - 1, put[i][1] - 1
    
    black, white = 0, 0    

    # 대각선 (/) 체크
    