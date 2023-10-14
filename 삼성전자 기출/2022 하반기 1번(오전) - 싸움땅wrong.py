n, m, k = map(int, input().split()) # 그리드 격자 사이즈, 사람 수, 라운드 진행 횟수
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서

# 총 값에 대한 3차원 배열 만들기
grid = []
for _ in range (n):
    temp_input = list(map(list, input().split()))
    for i in range (n):
        temp_input[i][0] = int(temp_input[i][0])
    grid.append(temp_input)

# 플레이어 정보 입력 받기
location_grid = [[0 for _ in range (n)] for _ in range (n)] # 0이 아닌 값은 플레이어 번호 값을 뜻한다. (1 이상 m이하)
player_point = {(i + 1) : 0 for i in range (m)} # 플레이어 포인트 딕셔너리
player_stat = {(i + 1) : 0 for i in range (m)} # 플레이어 기본 능력치 딕셔너리
player_gun = {(i + 1) : 0 for i in range (m)} # 플레이어 현재 보유 총 딕셔너리
player_dir = {(i + 1) : 0 for i in range (m)} # 플레이어 현재 방향 딕셔너리
player_location = {(i + 1): [0, 0] for i in range (m)} # 플레이어 현재 위치 딕셔너리
for pnum in range (1, m + 1):
    p_x, p_y, p_dir, p_stat = map(int, input().split())
    location_grid[p_x - 1][p_y - 1] = pnum # 인덱스 보정
    player_location[pnum] = [p_x - 1, p_y - 1] # 인덱스 보정
    player_dir[pnum] = p_dir
    player_stat[pnum] = p_stat

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 이동
for _ in range (k): 
    # 플레이어 1번부터 순차적으로 진행한다.
    for pnum in range (1, m + 1):
        # print(pnum)
        # for line in location_grid:
        #     print(line)
        current_x, current_y = player_location[pnum]
        current_dir = player_dir[pnum]
        current_gun = player_gun[pnum]
        
        # 이동 먼저. 만약 격자 바깥이면 반대 방향으로 돌아서 이동한다.
        nx, ny = current_x + dxs[current_dir], current_y + dys[current_dir]
        if not is_range(nx, ny): # 여긴 사람 있든 없든 상관 없이 그리드 안에만 있으면 됨
            current_dir = (current_dir + 2) % 4
            nx, ny = current_x + dxs[current_dir], current_y + dys[current_dir]
        
        if location_grid[nx][ny] == 0: # 사람 없으면 우선 이동
            
            location_grid[current_x][current_y] = 0 # 없다고 만들어
            location_grid[nx][ny] = pnum # 이제 여기에 사람이 있다
            current_x, current_y = nx, ny # 위치 변동
            player_location[pnum] = [nx, ny]
            player_dir[pnum] = current_dir
            
            for idx in range (len(grid[nx][ny])):
                grid[nx][ny][idx] = int(grid[nx][ny][idx]) # '0'이 자꾸 들어가

            if len(grid[nx][ny]) != 0 and current_gun < sorted(grid[nx][ny])[-1]: # 총이 있고, 값이 더 큰 총이 있다면?
                grid[nx][ny].append(current_gun)
                grid[nx][ny].sort()
                player_gun[pnum] = grid[nx][ny].pop()
            
            continue
        
        elif location_grid[nx][ny] != 0: # 사람 있으면
            cmp_pnum = location_grid[nx][ny] # 싸울 플레이어 넘버
            
            player1 = player_stat[pnum] + player_gun[pnum]
            player2 = player_stat[cmp_pnum] + player_gun[cmp_pnum]
            
            win = True
            if player1 < player2:
                win = False
            elif player1 == player2 and player_stat[pnum] < player_stat[cmp_pnum]:
                win = False
            
            if win: # pnum 승
                # 점수 추가
                player_point[pnum] += abs(player1 - player2)
                
                # 컴페어 플레이어가 이동 준비
                cmp_dir = player_dir[cmp_pnum]
                cmp_x, cmp_y = nx, ny
                
                # 진 컴페어는 총 그 자리에 내려 놓고 딕셔너리에도 반영
                grid[cmp_x][cmp_y].append(player_gun[cmp_pnum])
                player_gun[cmp_pnum] = 0 
                
                # 피넘 플레이어도 이동하고 딕셔너리에 반영
                location_grid[current_x][current_y] = 0
                location_grid[nx][ny] = pnum
                current_x, current_y = nx, ny
                player_location[pnum] = [current_x, current_y]
                player_dir[pnum] = current_dir
                
                # 컴페어넘 이동하고 딕셔너리에도 반영
                tx, ty = cmp_x + dxs[cmp_dir], cmp_y + dys[cmp_dir]
                while not is_range(tx, ty) or location_grid[tx][ty] != 0: 
                    cmp_dir = (cmp_dir + 1) % 4
                    tx, ty = cmp_x + dxs[cmp_dir], cmp_y + dys[cmp_dir]
                
                # location_grid[cmp_x][cmp_y] = 0 # 0으로 만들면 안 되지 그럼 이긴 애의 좌표도 없어지잖아
                location_grid[tx][ty] = cmp_pnum
                player_dir[cmp_pnum] = cmp_dir
                player_location[cmp_pnum] = [tx, ty]
                
                # 컴페어넘 총먹기
                if len(grid[tx][ty]) != 0 and player_gun[cmp_pnum] < sorted(grid[tx][ty])[-1]: # 총이 있고, 값이 더 큰 총이 있다면?
                    grid[tx][ty].append(player_gun[cmp_pnum])
                    grid[tx][ty].sort()
                    player_gun[cmp_pnum] = grid[tx][ty].pop()
                
                # 이긴 애는 총 먹기    
                if player_gun[pnum] < sorted(grid[nx][ny])[-1]:
                    grid[nx][ny].append(player_gun[pnum])
                    grid[nx][ny].sort()
                    player_gun[pnum] = grid[nx][ny].pop()
                    
            elif not win: # cmp_pnum 승일 땐 cmp_pnum은 가만히 있고 pnum만 움직여야 함
                # 점수 추가
                player_point[cmp_pnum] += abs(player2 - player1)
                
                # 총 그 자리에 내려놓기
                grid[nx][ny].append(player_gun[pnum])
                player_gun[pnum] = 0
                
                # 피넘 이동하고 딕셔너리에도 반영                
                location_grid[current_x][current_y] = 0
                tx, ty = nx + dxs[current_dir], ny + dys[current_dir]
                while not is_range(tx, ty) or location_grid[tx][ty] != 0:
                    current_dir = (current_dir + 1) % 4    
                    tx, ty = nx + dxs[current_dir], ny + dys[current_dir]
                    # print(tx, ty, "d")
                location_grid[tx][ty] = pnum
                player_dir[pnum] = current_dir
                player_location[pnum] = [tx, ty]
                
                # 피넘 총 줍기
                if len(grid[tx][ty]) != 0 and player_gun[pnum] < sorted(grid[tx][ty])[-1]:
                    grid[tx][ty].append(player_gun[pnum])
                    grid[tx][ty].sort()
                    player_gun[pnum] = grid[tx][ty].pop()

                # 이긴 애는 총 먹기
                if player_gun[cmp_pnum] < sorted(grid[nx][ny])[-1]:
                    grid[nx][ny].append(player_gun[cmp_pnum])
                    grid[nx][ny].sort()
                    player_gun[cmp_pnum] = grid[nx][ny].pop()
    for line in location_grid:
        print(line)    
    for line in grid:
        print(line)
    print(player_point)
    print()
    if _ == 6:
        exit(0)

for score in player_point.values():
    print(score, end=" ")
    
# 16 7 500
# 7 0 2 3 0 8 7 7 6 1 4 6 10 3 9 9
# 10 10 9 3 6 3 7 2 10 1 0 6 9 7 2 7
# 10 7 3 4 6 6 1 3 4 5 9 7 5 0 4 3
# 7 2 5 3 7 0 0 2 1 8 6 1 2 0 7 6
# 9 3 0 2 10 1 2 5 6 2 7 7 0 0 1 6
# 1 5 2 10 1 4 8 8 3 5 3 4 2 6 7 0
# 3 2 2 9 9 7 8 5 4 3 6 8 0 8 0 5
# 7 9 3 10 2 2 2 0 0 7 5 1 7 10 10 10
# 0 0 2 5 2 0 3 1 1 8 8 4 1 3 1 0
# 8 1 2 0 0 0 1 9 10 9 4 3 5 4 0 9
# 6 7 3 6 6 3 5 8 6 3 0 2 4 5 3 0
# 5 0 3 6 3 1 0 0 7 4 5 0 4 6 9 0
# 10 9 5 4 6 4 7 2 10 5 10 2 1 6 3 9
# 1 0 3 8 2 1 0 3 2 1 6 9 8 6 2 8
# 1 7 4 3 1 3 7 0 6 6 5 0 8 5 3 9
# 5 5 10 10 0 7 7 0 2 2 0 6 7 6 7 3
# 10 4 2 2
# 12 16 0 13
# 8 8 1 3
# 15 8 1 5
# 4 14 0 19
# 12 7 3 9
# 11 16 2 17
