# 숫자 0과 1로만 이루어진 n * n 크기의 격자 상태가 주어집니다. 
# 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수를 세는 프로그램을 작성해보세요. 
# 단, 인접한 곳이 격자를 벗어나는 경우에는 숫자 1이 적혀있지 않은 것으로 생각합니다.

# 첫 번째 줄에 n이 주어집니다.
# 두 번째 줄부터는 n개의 줄에 걸쳐 각 줄마다 각각의 행에 해당하는 n개의 숫자가 공백을 사이에 두고 주어집니다. 전부 0과 1로 이루어져 있다고 가정해도 좋습니다.
# 1 ≤ n ≤ 100

# 입력
# 4
# 0 1 0 1
# 0 0 1 1
# 0 1 0 1
# 0 0 1 0

# 출력: 4

n = int(input())
a = []
for _ in range (n):
    a.append(list(map(int, input().split())))

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북

def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

answer = 0

for x in range (n):
    for y in range (n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and a[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            answer += 1
print(answer)