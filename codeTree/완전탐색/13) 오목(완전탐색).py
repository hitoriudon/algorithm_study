def check(n1, n2, n3, n4, n5):
    return (n1 != 0 and n2 != 0 and n3 != 0 and n4 != 0 and n5 != 0) and (n1 == n2 == n3 == n4 == n5)

def is_range1(x):
    return x + 4 < 19

def is_range2(y):
    return y + 4 < 19

board = [list(map(int, input().split())) for _ in range (19)]

flag = False
# answer을 리스트에 담아야 하나?
for i in range (19):
    for j in range (19):
        # 가로 체크
        if is_range2(j) and check(board[i][j], board[i][j+1], board[i][j+2], board[i][j+3], board[i][j+4]):
            print(board[i][j+2])
            print(i+1, j+3)
            flag = True
            break
        # 세로 체크
        if is_range1(i) and check(board[i][j], board[i+1][j], board[i+2][j], board[i+3][j], board[i+4][j]):
            print(board[i+2][j])
            print(i+3, j+1)
            flag = True
            break
        # 대각선 체크 (왼->오)
        if is_range1(i) and is_range2(j) and check(board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4]):
            print(board[i+2][j+2])
            print(i+3, j+3)
            flag = True
            break        
        # 대각선 체크 (오->왼)
        if is_range1(i) and is_range2(j) and check(board[i+4][j], board[i+3][j+1], board[i+2][j+2], board[i+1][j+3], board[i][j+4]):
            print(board[i+2][j+2])
            print(i+3, j+3)
            flag = True
            break
if flag == False:
    print(0)