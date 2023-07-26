# (0, 0)에서 시작하여 총 N번 움직여보려고 합니다. N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어지고, 1초에 한 칸씩 움직인다고 했을 때, 
# 몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단하는 프로그램을 작성해보세요.

# 첫 번째 줄에 정수 N이 주어집니다.
# 두 번째 줄부터는 N개의 줄에 걸쳐 각 줄마다 이동방향과 이동한 거리가 공백을 사이에 두고 주어집니다. 
# 방향은 W, S, N, E중에 하나이며 각각 서, 남, 북, 동쪽으로 이동함을 의미합니다.
# 1 ≤ N ≤ 100
# 1 ≤ 한 번에 움직이는 거리 ≤ 10

# 첫 번째 줄에 다시 시작점으로 되돌아오는 데 걸리는 시간을 출력합니다. 만약 N번 이동을 진행했는데도 시작점으로 돌아오지 못했다면 -1을 출력합니다.

# 입력: 6
# N 3
# E 2
# S 3
# W 4
# S 5
# E 8

# 출력: 10

n = int(input())

command = []
for _ in range (n):
    command.append(list(map(str, input().split())))

dic = {'E': 0, 'W': 1, 'S': 2, 'N': 3}
x, y = 0, 0
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

t = 0
flag, loop_end_flag = False, False
for i in range (n):
    dir, dist = dic[command[i][0]], int(command[i][1])
    for j in range (dist):
        nx, ny = x + dxs[dir], y + dys[dir]
        if nx == ny == 0:
            flag = True
            t += 1
            break
        else:
            x, y = nx, ny
            t += 1
    if flag == True:
        loop_end_flag = True
        break
print(t if loop_end_flag == True else -1)