# 14503, 로봇 청소기, G5
n, m = map(int, input().split())
x, y, dir = map(int, input().split())
room = [list(map(int, input().split())) for _ in range (n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서
clean = 0

def four_way_check(x, y, dir):
    for i in range (1, 5):
        dir = (dir - 1) % 4
        nx, ny = x + dxs[dir], y + dys[dir]
        if room[nx][ny] == 0:
            return dir
    return -1 # 리턴값이 -1이라면 주위에 닦을 곳이 없는 것
    
while True:
    if room[x][y] == 0:
        room[x][y] = 2 # 닦았다
        clean += 1
    
    flag = four_way_check(x, y, dir)
    if flag != -1:
        dir = flag
        x, y = x + dxs[dir], y + dys[dir] # new_x, new_y
        continue
    elif flag == -1:
        x, y = x - dxs[dir], y - dys[dir] # 백무빙
        if room[x][y] == 1:
            print(clean)
            break

# 완전탐색, 23분
# 이건 쉬운듯 걍 코드트리에 있는 완탐보다 훨씬 쉬운 거 같아
# 구현, 시뮬레이션