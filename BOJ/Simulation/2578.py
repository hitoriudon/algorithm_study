# 2578, 빙고, S4
# 빙고 게임, 3줄 완성 시에 빙고

board = []
for _ in range (5):
    board.append(list(map(int, input().split())))

numbers = []
for _ in range (5):
    lst = list(map(int, input().split()))
    for l in lst:
        numbers.append(l)

answer = 0
for n in numbers:
    loop_flag = False
    cnt = 0
    for i in range (5):
        for j in range (5):
            if board[i][j] == n:
                board[i][j] = -1
                loop_flag = True
                break
        if loop_flag: 
            break
    answer += 1
    
    for i in range (5):
        # 가로 체크 
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == -1:
            cnt += 1
        # 세로 체크
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == -1:
            cnt += 1        
    # 대각선 체크
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == -1:
        cnt += 1
    if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] == -1:
        cnt += 1
    if cnt >= 3:
        break
print(answer)