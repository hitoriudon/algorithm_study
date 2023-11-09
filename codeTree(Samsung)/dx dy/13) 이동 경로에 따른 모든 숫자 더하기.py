# N * N크기의 정사각형 모양의 격자 정보가 주어졌을 때, 가운데 위치에서 북쪽을 향한 상태로 움직이는 것을 시작하려 합니다.
# T개의 명령에 따라 움직이며, 명령어는 L,R,F로 주어집니다. 명령 L은 왼쪽으로 90도 방향 전환을, 명령 R은 오른쪽으로 90도 방향 전환을, 
# 명령 F가 주어지면 바라보고 있는 방향으로 한칸 이동하게 됩니다. 
# 시작 위치를 포함하여 위치를 이동하게 될 때마다 해당 칸에 적혀있는 수를 계속 더한다고 헀을 때
# 이들의 총합을 구하는 프로그램을 구하는 프로그램을 작성해보세요.
# 단, 격자의 범위를 벗어나게 하는 명령어는 무시해야함에 유의합니다.

# 첫 번째 줄에 정수 N과 T가 공백을 사이에 두고 주어집니다.
# 두 번째 줄에 문자 L, R, 그리고 F로만 이루어진 문자열이 하나 주어집니다.
# 세 번째 줄부터 N개의 줄에 걸쳐 각 행에 해당하는 n개의 수들이 공백을 사이에 두고 주어집니다.
# 3 ≤ N ≤ 99 (단, N은 홀수)
# 1 ≤ T ≤ 100,000
# 1 ≤ 격자 안의 수 ≤ 9

# 입력:
# 3 8
# RFFFLFLF
# 1 2 3
# 4 5 6
# 7 8 9

# 출력: 16

n, t = map(int, input().split())
command = list(str(input()))
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서
dir = 0 # 북쪽
x = y = n // 2
board = []
for _ in range (n):
    board.append(list(map(int, input().split())))

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

total = board[x][y]
for c in command:
    if c == 'L':
        dir = (dir - 1) % 4
    elif c == 'R':
        dir = (dir + 1) % 4
    else:
        nx, ny = x + dxs[dir], y + dys[dir]
        if is_range(nx, ny):
            total += board[nx][ny]
            x, y = nx, ny
print(total)