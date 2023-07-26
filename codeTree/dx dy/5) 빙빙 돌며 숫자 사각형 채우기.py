# n * m크기의 직사각형에 숫자 1부터 순서대로 증가시키며 달팽이 모양으로 채우는 코드를 작성해보세요.
# 달팽이 모양이란 왼쪽 위 모서리에서 시작해서, 오른쪽, 아래쪽, 왼쪽, 위쪽 순서로 더 이상 채울 곳이 없을 때까지 회전하는 모양을 의미합니다.
# n : 행(row), m : 열(column)을 의미합니다.

# n과 m이 공백을 사이에 두고 주어집니다.
# 1 ≤ n, m ≤ 100

# 입력: 4 4
# 출력: 
# 1 2 3 4
# 12 13 14 5 
# 11 16 15 6 
# 10 9 8 7

n, m = map(int, input().split())

a = []
for _ in range (n):
    a.append([0] * m) 
    
x, y = 0, 0 # 현재 포지션
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
dir = 0

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

a[x][y] = 1
i = 1
while i < n * m:
    nx, ny = x + dxs[dir], y + dys[dir]
    if is_range(nx, ny) and a[nx][ny] == 0:
        a[nx][ny] = i + 1
        x, y = nx, ny
        i += 1
    else: 
        dir = (dir + 1) % 4

for lst in a:
    for l in lst:
        print(l, end=" ")
    print()
    