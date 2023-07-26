# N * N 크기의 격자 위에 총 M번에 걸쳐 색칠을 진행합니다. 한 번에 한 칸만 색칠하며, 색칠을 한 직후 해당 칸이 '편안한 상태'에 놓여 있는지를 확인하려 합니다. 
# ‘편안한 상태’란 방금 막 칠해진 칸을 기점으로 위 아래 양옆으로 인접한 4개의 칸 중 격자를 벗어나지 않는 칸에 색칠되어 있는 칸이 정확히 3개인 경우를 뜻합니다. 
# 색칠할 칸이 주어질 때마다 해당 칸을 칠한 직후 막 칠한 칸이 편안한 상태에 있는지를 계속 알아내는 프로그램을 작성해보세요.

# 첫 번째 줄에는 정수 N과 M이 주어집니다.
# 두 번째 줄부터는 M개의 줄에 걸쳐 각 줄마다 색칠할 칸의 위치 (r, c) 가 공백을 사이에 두고 주어집니다. 
# 이는 r행 c열에 색칠해야 함을 의미하며, 색칠을 동일한 칸에 2번 이상 하게되는 경우는 없다고 가정해도 좋습니다.
# 1 ≤ N ≤ 100
# 1 ≤ M ≤ N * N
# 1 ≤ r, c ≤ N

# 입력
# 4 8
# 1 2
# 2 1
# 2 3
# 2 2
# 3 3
# 4 2
# 3 2
# 4 3

# 출력
# 0
# 0
# 0
# 1
# 0
# 0
# 1
# 0

n, m = map(int, input().split())
a = []
for _ in range (n):
    a.append([False] * n)

command = []
for _ in range (m):
    command.append(list(map(int, input().split())))
    
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for c in command:
    x, y = c[0] - 1, c[1] - 1
    a[x][y] = True # 색칠
    cnt = 0
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and a[nx][ny] == True:
            cnt += 1
    print(0 if cnt != 3 else 1)