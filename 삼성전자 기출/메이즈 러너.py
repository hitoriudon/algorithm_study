from copy import deepcopy
def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def find_exit_location():
    for i in range (n):
        for j in range (n):
            if grid[i][j][1] == '10': # 출구 값
                return (i, j)
def find_people_location():
    temp = []
    for i in range (n):
        for j in range (n):
            if type(grid[i][j][1]) == int and grid[i][j][1] > 0:
                temp.append((i, j))
    return temp

def can_exit(x, y):
    grid[x][y][1] = 0

def find_people():
    cnt = 0
    for i in range (n):
        for j in range (n):
            if (grid[i][j][1]) != 0:
                cnt += 1
    return cnt > 1

def moving(loc): 
    # 모든 사람 움직임
    global ans
    temp_loc = deepcopy(loc)
    for i in range (len(loc)):
        x, y = loc[i]
        # for line in grid:
        #     for num in line:
        #         print(num, end=" ")
        #     print()
        # print()
        if x != exit_x:
            nx, ny = x, y # 임시
                
            if x > exit_x:
                nx -= 1
            elif x < exit_x:
                nx += 1
            
            if grid[nx][ny][0] == 0:
                ans += grid[x][y][1]
                temp_loc[i] = (nx, ny)
                # if grid[nx][ny][1] == '10':
                #     can_exit(x, y)
                #     continue
                # grid[nx][ny][0], grid[nx][ny][1] = grid[x][y][0], grid[nx][ny][1] + grid[x][y][1]
                # grid[x][y][0], grid[x][y][1] = 0, 0
                continue
            
        if y != exit_y:
            nx, ny = x, y # 임시
        
            if y > exit_y:
                ny -= 1
            elif y < exit_y:
                ny += 1
            
            if grid[nx][ny][0] == 0:
                ans += grid[x][y][1]
                temp_loc[i] = (nx, ny)
                # if grid[nx][ny][1] == '10':
                #     can_exit(x, y)
                #     continue
                # grid[nx][ny][0], grid[nx][ny][1] = grid[x][y][0], grid[nx][ny][1] + grid[x][y][1]
                # grid[x][y][0], grid[x][y][1] = 0, 0
                continue
    for i in range (len(loc)):
        if loc[i][0] == temp_loc[i][0] and loc[i][1] == temp_loc[i][1]:
            continue
        else:
            nx, ny = temp_loc[i]
            x, y = loc[i]
            if grid[nx][ny][1] == '10':
                can_exit(x, y)
                continue
            grid[nx][ny][0], grid[nx][ny][1] = grid[x][y][0], grid[nx][ny][1] + grid[x][y][1]
            grid[x][y][0], grid[x][y][1] = 0, grid[x][y][1] - 1
        
def find_rect(): # 미친 완탐
    for size in range (2, n + 1):
        for i in range (n): # 시작점 완탐 x
            for j in range (n): # 시작점 완탐 y
                sliced = []
                for k in range (i, i + size):
                    temp = []
                    for l in range (j, j + size):
                        if is_range(k, l):
                            temp.append(grid[k][l])
                    if len(temp) == size:
                        sliced.append(temp)
                if len(sliced) == size:
                    if check(sliced):
                        value_list, flag_list = [], []
                        for a in range (len(sliced)):
                            value_temp, flag_temp = [], []
                            for b in range (len(sliced)):
                                if sliced[a][b][0] > 0:
                                    value_temp.append(sliced[a][b][0] - 1)
                                else:
                                    value_temp.append(0)
                                flag_temp.append(sliced[a][b][1])
                            value_list.append(value_temp)
                            flag_list.append(flag_temp)
                        value_list = list(zip(*value_list[::-1]))
                        flag_list = list(zip(*flag_list[::-1]))
                        
                        for a in range (len(sliced)):
                            for b in range (len(sliced)):
                                grid[i + a][b + j][0] = value_list[a][b]
                                grid[i + a][b + j][1] = flag_list[a][b]
                        # for line in sliced:
                        #     for num in line:
                        #         print(num, end=" ")
                        #     print() 
                        # print()
                                    
                        return
                    
def check(graph): # 자른 3차원 배열
    p, e = False, False
    for i in range (len(graph)):
        for j in range (len(graph)):
            if graph[i][j][1] == '10': # 출구 있음
                e = True
            elif (graph[i][j][1]) > 0: # 사람 있음
                p = True
    return e == p == True
n, m, k = map(int, input().split())

# 사람이 있는 곳은 옆에 하나 더 둘 거야
grid = [] 
for _ in range (n):
    nums = list(map(int, input().split()))
    temp = []
    for num in nums:
        temp.append([num, 0])
    grid.append(temp)

people = [tuple(map(int, input().split())) for _ in range (m)]
exit = tuple(map(int, input().split()))

# 사람 위치 표시
idx = 0
for person in people:
    x, y = person
    grid[x - 1][y - 1][1] += 1 # 인덱스 보정, 사람 인원 수

# 출구 위치 표시
grid[exit[0] - 1][exit[1] - 1][1] = '10' # 인덱스 보정, '10'은 출구가 있다

ans = 0
for t in range (k):
    
    exit_x, exit_y = find_exit_location()
    current_people_location = find_people_location()

    moving(current_people_location)
    for line in grid:
        for num in line:
            print(num, end=" ")
        print()
    print()
    if not find_people():
        print("no one")
        break
    
    find_rect()
    for line in grid:
        for num in line:
            print(num, end=" ")
        print()
    print()
fx, fy = find_exit_location()
print(ans)
print(fx + 1, fy + 1)

# 4 6 1
# 9 6 2 9
# 0 0 0 0
# 3 4 0 0
# 0 0 9 2
# 2 2
# 3 3
# 4 2
# 2 3
# 4 2
# 4 2
# 4 1
