from copy import deepcopy

def is_range(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

eat_dxs, eat_dys = [-1, 0, 1, 0], [0, -1, 0, 1] # 상 좌 하 우
arr = []
def f(level, begin, x, y):
    if level == 3:
        if len(arr) == 3:
            vis = []
            
            # 먹는 걸 진행한다
            cnt = 0

            for a in arr:
                x, y = x + eat_dxs[a], y + eat_dys[a]
                if is_range(x, y) and len(grid[x][y]) > 0 and (x, y) not in vis:
                    cnt += len(grid[x][y])
                    vis.append((x, y))
            eat.append(((-1) * cnt, arr[0], arr[1], arr[2]))
        return
    for i in range (begin, 4):
        arr.append(i)
        f(level + 1, begin, x, y)
        arr.pop()
    f(level + 1, begin + 1, x, y)
    
dxs = [-1, -1, 0, 1, 1, 1, 0, -1] # 북 북서 서 서남 남 남동 동 동북
dys = [0, -1, -1, -1, 0, 1, 1, 1] # 북 북서 서 서남 남 남동 동 동북

m, t = map(int, input().split())
px, py = map(int, input().split()) # packman
px, py = px - 1, py - 1 # 인덱스 보정

grid = [[[] for _ in range (4)] for _ in range (4)] # 몬스터 정보에 대한 배열을 담을 3차원 배열
deads = [[0 for _ in range (4)] for _ in range (4)] # 그 자리에 시체가 있는지 확인. 죽으면 값을 2로 초기화 하고, 한 턴이 지날 때마다 0이 아닌 값들은 -1 해줘야 함.
monster = []
for i in range (m):
    r, c, d = map(int, input().split())
    monster.append([r - 1, c - 1, d - 1]) # 인덱스 보정

    grid[r - 1][c - 1].append(monster[i]) # 몬스터 정보 배열을 그리드에 담기

# 팩맨이 먹을 때 실행되는 백트래킹 함수

for turn in range (t):
    # 1초 감소 0 이상인 애들만
    for i in range (4):
        for j in range (4):
            if deads[i][j] > 0:
                deads[i][j] -= 1

    # 몬스터 복제 시도
    copy_grid = deepcopy(grid) # 여기에 알 까기 성공.
    
    # 몬스터 이동
    # for line in grid:
    #     print(line)
    
    for i in range (len(monster)):
        bx, by, bdir = monster[i] # 움직이기 전(before) 몬스터 위치, 그리고 방향

        for idx in range (8):
            ndir = (bdir + idx) % 8
            nx, ny = bx + dxs[ndir], by + dys[ndir]
            # nx, ny, ndir = bx + dx, by + dy, (bdir + idx) % 8
            if is_range(nx, ny) and not (nx == px and ny == py) and deads[nx][ny] == 0:
                # 이동
                pop_idx = grid[bx][by].index([bx, by, bdir]) # 현재 그리드 위치에서 꺼내서
                grid[nx][ny].append([nx, ny, ndir]) # 이동해야 할 그리드 위치에 넣어주기
                grid[bx][by].pop(pop_idx) # 빼주기
                monster[i] = [nx, ny, ndir] # 정보 변경
                break # 이동 멈추기
        
        # 8번 다 돌았는데도 안 되면 이동 안 하니까 그냥 스탑
    
    # for line in grid:
    #     print(line)
    # print()
    # print(monster, px, py)
    
    # 팩맨 이동, 팩맨 위치 변경
    eat = []
    f(0, 0, px, py)
    # print(sorted(eat))
    # print()
    # eaten, move1, move2, move3 = sorted(eat)[0] # eaten은 안 쓰임
    for eaten, move1, move2, move3 in sorted(eat):
        
        pxmove = [px + eat_dxs[move1], px + eat_dxs[move1] + eat_dxs[move2], px + eat_dxs[move1] + eat_dxs[move2] + eat_dxs[move3]]
        pymove = [py + eat_dys[move1], py + eat_dys[move1] + eat_dys[move2], py + eat_dys[move1] + eat_dys[move2] + eat_dys[move3]]
        egg_loc = list(set(zip(pxmove, pymove)))
        flag = False
        for egg_x, egg_y in egg_loc:
            if egg_x < 0 or egg_x >= 4 or egg_y < 0 or egg_y >= 4:
                flag = True
                break
        if flag:
            continue
        
        else:
            # 팩맨 시체 타임 추가
            for rx, ry in egg_loc:
                deads[rx][ry] += 2
            
            moves = [move1, move2, move3]
            for move in moves:
                # 팩맨 한 칸 전진
                px += eat_dxs[move]
                py += eat_dys[move]
                
                # 몬스터 사망 처리
                removed = grid[px][py]
                for ridx in range (len(removed)):
                    rx, ry, rdir = removed[ridx]
                
                # 팩맨 시체 타임 추가
                # deads[px][py] += 2 # 이거 아닌듯
                grid[px][py] = []
                for ridx in range (len(monster)):
                    if px == monster[ridx][0] and py == monster[ridx][1]:
                        monster[ridx] = [-1, -1, -1] # 사망 처리
            break
    # print(monster)
    monster = list(filter(lambda x: x[0] > -1 and x[1] > -1 and x[2] > -1, monster)) # 사망한 몬스터는 몬스터 배열에서 제외
    
    # 부화한 애들 몬스터 배열에 추가 (몬스터 복제)
    for i in range (4):
        for j in range (4):
            if len(copy_grid[i][j]) > 0: # 알이 있으면
                for k in range (len(copy_grid[i][j])):
                    monster.append(copy_grid[i][j][k])
                    
    temp_grid = [[[] for _ in range (4)] for _ in range (4)]
    for mx, my, mdir in monster:
        temp_grid[mx][my].append([mx, my, mdir])
    grid = deepcopy(temp_grid)
    
print(len(monster))
# 정답: 10
# 4 3
# 4 4
# 2 2 7
# 4 4 7
# 4 2 8
# 1 3 5

