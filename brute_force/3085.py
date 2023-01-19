def check():
    board_max = 1
    for n in range (N):
        max_row, max_col = 1, 1
        for k in range (N-1):
            if board[n][k] == board[n][k+1]:
                max_row += 1
                board_max = max(max_row, board_max) # 난 마지막에 체크했는데, 왜 계속 체크해 나가야 하는 걸까?
            elif board[n][k] != board[n][k+1]:
                max_row = 1
        for k in range (N-1):
            if board[k][n] == board[k+1][n]:
                max_col += 1
                board_max = max(max_col, board_max) # 반례도 없었는데.. 뭘까
            elif board[k][n] != board[k+1][n]:
                max_col = 1
    return board_max

import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range (N)]
current_max = 1

for i in range (N): #세로
    for j in range (N): #가로
        if j < N - 1:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            tmp = check()
            if current_max < tmp:
                current_max = tmp
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i < N - 1:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp = check()
            if current_max < tmp:
                current_max = tmp
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(current_max)

# check()에서, max(행 맥시멈, 현재 맥시멈) 값을 k 포문 두 개가 끝나면 체크했는데,
# 포문 안에서 계속 체크해줘야했다.. 이유는 모름