# 1개의 구슬이 n*n 격자 안에 놓여져 있고, 격자는 벽으로 둘러싸여 있습니다. 이 구슬은 방향을 갖고 있고, 해당 방향으로 1초에 한칸 씩 움직입니다.
# 구슬의 처음 위치와 초기 방향이 주어졌을 때, t초가 지난 이후에 해당 구슬의 위치를 구하는 프로그램을 작성해보세요.

# 첫 번째 줄에는 격자의 크기를 나타내는 n과 시간 t가 공백을 사이에 두고 주어집니다.

# 두 번째 줄에는 구슬 정보 (r, c, d)가 공백을 사이에 두고 주어집니다.
# 현재 구슬이 r행 c열에 놓여 있으며, d방향을 바라보고 있음을 뜻합니다. d는 위 아래 오른쪽 왼쪽을 의미하는 
# ‘U', ‘D’, ‘R’, 'L’ 4개의 문자 중 하나가 주어집니다. (1 ≤ r ≤ n, 1 ≤ c ≤ n)
# 2 ≤ n ≤ 50
# 1 ≤ t ≤ 100

# 입력
# 4 4
# 1 2 L

# 출력
# 1 3

n, t = map(int, input().split())
r, c, d = map(str, input().split())

loc = {'D': 0, 'L': 1, 'R': 2, 'U': 3}
dxs, dys = [1, 0, 0, -1], [0, -1, 1, 0] # Down Left Right Up

r, c = int(r), int(c)

def is_range(x, y):
    return x > 0 and y > 0 and x <= n and y <= n

current_direction = loc[d]
for i in range (t):
    nr, nc = r + dxs[current_direction], c + dys[current_direction]
    if not is_range(nr, nc):
        current_direction = 3 - current_direction
    else:
        r, c = nr, nc
print(r, c)