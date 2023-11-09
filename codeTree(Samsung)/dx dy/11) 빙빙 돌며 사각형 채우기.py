# n * m크기의 직사각형에 대문자 알파벳을 A부터 Z까지 순서대로 증가시키며 달팽이 모양으로 채우는 코드를 작성해보세요.
# 달팽이 모양이란 왼쪽 위 모서리에서 시작해서, 오른쪽, 아래쪽, 왼쪽, 위쪽 순서로 더 이상 채울 곳이 없을 때까지 회전하는 모양을 의미합니다.
# Z 이후에는 다시 A부터 채우기 시작합니다.
# n : 행(row), m : 열(column)을 의미합니다.

# n과 m이 공백을 사이에 두고 주어집니다.
# 1 ≤ n, m ≤ 100

# 입력: 4 4
# 출력
# A B C D 
# L M N E 
# K P O F 
# J I H G

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, m = map(int, input().split())

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
x, y, dir = 0, 0, 0

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

board = []
for _ in range (n):
    board.append([0 for _ in range (m)])

board[x][y] = "A"
i = 1
while i < n * m:
    nx, ny = x + dxs[dir], y + dys[dir]
    if is_range(nx, ny) and board[nx][ny] == 0:
        board[nx][ny] = alphabet[i % 26]
        i += 1
        x, y = nx, ny
    else:
        dir = (dir + 1) % 4

for arr in board:
    for a in arr:
        print(a, end=" ")
    print()