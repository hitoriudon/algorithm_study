# N * N 크기의 격자 안에 각 칸마다 거울이 하나씩 들어 있습니다. 각 거울은 \나 /의 형태를 띄고있고, 
# 격자 밖 4N개의 위치 중 특정 위치에서 레이저를 쏘았을 때, 거울에 튕기는 횟수를 구하는 프로그램을 작성해보세요.

# 첫 번째 줄에 N이 주어집니다.
# 두 번째 줄부터 N개의 줄에 걸쳐 맵의 정보가 주어집니다. 각 줄에는 각 행에 해당하는 정보가 공백없이 주어집니다. 
# 이는 /나 \ 문자로만 이루어져 있습니다.
# 그 다음 줄에는 레이저를 쏘는 위치 K가 주어집니다. K는 다음과 같이 위에서 아래 방향으로 1행 1열 칸으로 들어오는 곳을 1번으로 하여 
# 시계 방향으로 돌며 가능한 시작 위치에 순서대로 번호를 붙여 4N 번을 마지막으로 했을 때의 번호들 중 하나의 값으로 주어집니다.

# 1 ≤ N ≤ 1,000
# 1 ≤ K ≤ 4N

# 입력: 
# 3
# /\\
# \\\
# /\/
# 2
# 출력: 3

n = int(input())
arr = []
for _ in range (n):
    string = input()
    arr.append(list(string))
    
k = int(input())
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # N E S W (시계 방향)

start_direction = (k - 1) // n # 첫 방향 잡기
dir = (2 + start_direction) % 4 # 북쪽에서 시작하면 S로 가야하니까

# 스타팅 x, y 잡기
starts = {}
for i in range (4):
    for j in range (1, n + 1):
        tmp = n * i + j
        a, b = 0, 0
        if i == 0:
            a, b = i, j - 1
        elif i == 1:
            a, b = j - 1, n - 1
        elif i == 2:
            a, b = n - 1, n - j
        else:
            a, b = n - j, 0
        starts[tmp] = (a, b)       

x, y = starts[k]

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

answer = 0
while True:
    if is_range(x, y) == False:
        break
    elif is_range(x, y) and arr[x][y] == '\\':
        if dir == 2:
            dir = 1
        elif dir == 3:
            dir = 0
        elif dir == 0:
            dir = 3
        else:
            dir = 2
    elif is_range(x, y) and arr[x][y] == '/':
        if dir == 2:
            dir = 3
        elif dir == 3:
            dir = 2
        elif dir == 0:
            dir = 1
        else:
            dir = 0
    x, y = x + dxs[dir], y + dys[dir]
    
    answer += 1
print(answer)