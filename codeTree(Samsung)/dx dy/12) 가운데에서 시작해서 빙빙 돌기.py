# n * n크기의 직사각형의 가운데에서 시작하여 오른쪽, 위, 왼쪽, 아래 순서로 더 이상 채울 곳이 없을 때까지 회전하며 숫자를 적어나가려고 합니다.
# 숫자는 1부터 시작한다고 했을 때, 다음과 같은 모양으로 숫자들을 쭉 채우는 코드를 작성해보세요.

# 첫 번째 줄에 크기를 나타내는 n이 주어집니다. 주어지는 n은 항상 홀수라고 가정해도 좋습니다.
# 1 ≤ n ≤ 100

# 입력: 3
# 출력
# 5 4 3
# 6 1 2
# 7 8 9

n = int(input())
board = []
for _ in range (n):
    board.append([0 for _ in range (n)])

dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0] # 서 북 동 남
x = y = n - 1
dir, i = 0, n ** 2

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n 

board[x][y] = i

while i > 1:
    nx, ny = x + dxs[dir], y + dys[dir]
    if is_range(nx, ny) and board[nx][ny] == 0:
        i -= 1
        board[nx][ny] = i
        x, y = nx, ny
    else:
        dir = (dir + 1) % 4
    
for arr in board:
    for a in arr:
        print(a, end=" ")
    print()