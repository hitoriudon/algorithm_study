from copy import deepcopy

def draw_line(l, temp_arr): # 0으로 가득 찬 2차원 배열을 선으로(값 1로 변경) 연결
    for x, y in l:
        temp_arr[y - 1][2 * x - 2], temp_arr[y - 1][2 * x - 1] = 1, 1
    return temp_arr

def is_range(x, y): # 필수 조건
    return x >= 0 and x < length and y >= 0 and y < 2 * n - 1

# main
n, m = map(int, input().split())
line = [tuple(map(int, input().split())) for _ in range (m)]

# grid 세로 길이 최저로 측정하려고 함
length = sorted(line, key = lambda x : x[1], reverse= True)[0][1] # 이 값을 grid 세로 길이로
grid = [[0 for _ in range (2 * n - 1)] for _ in range (length + 1)]
dxs, dys = [1, 1], [-2, 2] # <- <- 밑, -> -> 밑

main_grid = deepcopy(grid)
main_grid = draw_line(line, main_grid)

# 우선 결과부터 뽑고
for j in range (0, 2 * n - 1, 2):
    x, y = 0, j
    for _ in range (length):
        if is_range(x, y - 1) and main_grid[x][y - 1] == 1: # left
            x, y = x + dxs[0], y + dys[0]
        elif is_range(x, y + 1) and main_grid[x][y + 1] == 1: # right
            x, y = x + dxs[1], y + dys[1]
        else:
            x, y = x + 1, y
    main_grid[x][y] = j // 2 + 1

result = list(filter(lambda x: x > 0, main_grid[-1])) # 나와야 하는 결과

array = []
ans = m + 1

def f(cnt): # 재귀함수 기반 백트래킹
    global ans # 이거 없음 에러 남
    
    if cnt == m: # line 수
        new_grid = deepcopy(grid) # 빈 2차원 배열 copy
        new_grid = draw_line(array, new_grid) # 백트래킹으로 선택된 줄만 0에서 1로 변경
        
        for j in range (0, 2 * n - 1, 2): # 사다리 경로 탐색
            x, y = 0, j # start index
            for _ in range (length):
                if is_range(x, y - 1) and new_grid[x][y - 1] == 1: # left
                    x, y = x + dxs[0], y + dys[0]
                elif is_range(x, y + 1) and new_grid[x][y + 1] == 1: # right
                    x, y = x + dxs[1], y + dys[1]
                else:
                    x, y = x + 1, y # 그냥 한 칸 내려가기
            
            new_grid[x][y] = j // 2 + 1 # 사다리 한 줄 끝

        new_result = list(filter(lambda x: x > 0, new_grid[-1])) # 나와야 하는 결과        
        
        if new_result == result:            
            ans = min(ans, len(array))
        return m + 1 # 라인 개수 + 1을 리턴해서 min을 무시하도록
    
    # 백트래킹
    array.append(line[cnt])
    f(cnt + 1)
    array.pop()
    f(cnt + 1)

f(0)
print(ans)

# 해설 보니까
# 실제 사다리를 내려가는 걸 그래프 탐색을 통해 진행하지 않고
# 그냥 기본 main grid와 바꾼 grid가 같은지? 확인하는 거 같음
# 그니까 먼저 main grid를 그린 다음
# 그린 main grid에 새로운 라인들만 바꿔주는?