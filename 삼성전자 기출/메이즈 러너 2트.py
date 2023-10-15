from copy import deepcopy

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def rect():
    test_grid = [[0 for _ in range (n)] for _ in range (n)]
    for ti in range (n):
        for tj in range (n):
            if len(people_grid[ti][tj]) > 0:
                if people_grid[ti][tj][0] == [-1, -1]:
                    test_grid[ti][tj] = 2
                elif not people_grid[ti][tj][0] == [-2, -2]:
                    test_grid[ti][tj] = 1

    if turn == 45:
        print("here", turn)
        for line in test_grid:
            print(line)
        for line in people_grid:
            print(line)
        print("hidd", people_grid[9][3])
    for length in range (1, n):
        for x in range (n):
            for y in range (n):
                rx, ry = x + length, y + length
                if is_range(rx, ry):
                    sliced = []
                    for i in range (x, rx + 1):
                        temp = []
                        for j in range (y, ry + 1):
                            temp.append(test_grid[i][j])
                        sliced.append(temp)
                    # 슬라이스된 배열에서 출구랑 참가자랑 같이 있나 평가 시작
                    exit_flag, person_flag = False, False
                    for si in range (len(sliced)):
                        for sj in range (len(sliced)):
                            if sliced[si][sj] == 2:
                                exit_flag = True
                            elif sliced[si][sj] == 1:
                                person_flag = True
                    if exit_flag and person_flag:
                        return (x, y, rx, ry)
    print("return fasle", turn)
n, m, k = map(int, input().split())

walls = [list(map(int, input().split())) for _ in range (n)] 
        
people = [] # 참가자의 현재 위치 정보가 담겨있는 배열
people_grid = [[[] for _ in range (n)] for _ in range (n)]
for _ in range (m):
    r, c = map(int, input().split())
    people.append([r - 1, c - 1])
    people_grid[r-1][c-1].append([r-1, c-1])
ex, ey = map(int, input().split())
ex, ey = ex - 1, ey - 1

people_grid[ex][ey].append([-1, -1]) # 출구라는 뜻
# for line in people_grid:
#     print(line)
ans = 0
outs = 0
for turn in range (1, k+1):
    # 모든 참가자 이동
    for i in range (len(people)):
        bx, by = people[i][0], people[i][1] # before
        nx, ny = people[i][0], people[i][1]
        if nx != ex:
            if nx > ex:
                nx -= 1
            elif nx < ex:
                nx += 1
            
            if walls[nx][ny] == 0:
                people[i][0], people[i][1] = nx, ny
                ans += 1

                if nx == ex and ny == ey:
                    people_grid[bx][by].remove([bx, by])
                    people[i][0], people[i][1] = -2, -2
                    outs += 1
                continue        
        if ny != ey:
            if ny > ey:
                ny -= 1
            elif ny < ey:
                ny += 1
            
            if walls[nx][ny] == 0:
                people[i][0], people[i][1] = nx, ny
                ans += 1
                if nx == ex and ny == ey:
                    people_grid[bx][by].remove([bx, by])
                    people[i][0], people[i][1] = -2, -2
                    outs += 1
                continue
        # if turn == 23:
        #     print("sdf", bx, by, nx, ny, ex, ey)
        # # 여기가 안 돔
            # for a in range (len(people_grid[bx][by])):
            #     if people_grid[bx][by][a][0] != -1 and people_grid[bx][by][a][1] != -1:
            #         people_grid[bx][by][a] = [-2, -2]
            #         people[i][0], people[i][1] = -2, -2 # 이제 얜 안 봐도 된다
    # 전원 탈출?
    if outs == m:
        print(ans, turn)
        print(ex, ey)
        exit(0)
    
    if turn == 23: print("outs:", outs, ex, ey)
    # 회전하기 전에 people grid 최신화
    people_grid = [[[] for _ in range (n)] for _ in range (n)]
    for x, y in people:
        if not (x == -2 and y == -2):    
            people_grid[x][y].append([x, y])
    
    people_grid[ex][ey].append([-1, -1])
    if 5 < len(people) <= m:
        print(turn, ans, people)
        for line in walls:
            print(line)
        for line in people_grid:
            print(line)
        print()
    if turn == 23:
        for line in people_grid:
            print(line)
    # 회전 (walls와 people_grid 둘 다 회전 결과를 반영해야 함)
    rotate_start_x, rotate_start_y, rotate_end_x, rotate_end_y = rect()
    diff_x = rotate_start_x
    diff_y = rotate_start_y
   
    # walls부터 회전
    temp_wall = []
    for i in range (rotate_start_x, rotate_end_x + 1):
        tmp = []
        for j in range (rotate_start_y, rotate_end_y + 1):
            if walls[i][j] > 0:    
                tmp.append(walls[i][j] - 1)
            else:
                tmp.append(walls[i][j])
        temp_wall.append(tmp)
    temp_wall = list(zip(*temp_wall[::-1]))

    for i in range (rotate_end_x - rotate_start_x + 1):
        for j in range (rotate_end_y - rotate_start_y + 1):
            walls[i+diff_x][j+diff_y] = temp_wall[i][j]
    
    # 사람, 출구 위치를 가지고 있는 people_grid도 회전
    temp_grid = []
    for i in range (rotate_start_x, rotate_end_x + 1):
        tmp2 = []
        for j in range (rotate_start_y, rotate_end_y + 1):
            tmp2.append(people_grid[i][j])
        temp_grid.append(tmp2)
    temp_grid = list(zip(*temp_grid[::-1]))
    
    for i in range (rotate_end_x - rotate_start_x + 1):
        for j in range (rotate_end_y - rotate_start_y + 1):
            people_grid[i+diff_x][j+diff_y] = temp_grid[i][j]
    # if turn == 6:
    #     print(turn, people)
    #     print("here")
    #     for line in people_grid:
    #         print(line)
    temp_people = []
    for i in range (n):
        for j in range (n):
            if len(people_grid[i][j]) >= 1:
                for k in range (len(people_grid[i][j])):
                    if not (people_grid[i][j][k][0] == -1 and people_grid[i][j][k][1] == -1):
                        temp_people.append([i, j])
                        people_grid[i][j][k] = [i, j]
                    elif people_grid[i][j][k][0] == -1 and people_grid[i][j][k][1] == -1:
                        ex, ey = i, j
    people = deepcopy(temp_people)
    # if turn == 6:
    #     print(turn, people)

print(ans)
print(ex + 1, ey + 1)