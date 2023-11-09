from copy import deepcopy

n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북 (순서 상관 없어서)

def Print(array):
    for line in array:
        for num in line:
            print(num, end=" ")
        print()
    print()
    
def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def find_the_optimum(x, y, array): # 한 점에 대한 인접 격자 최적의 쌍 개수 리턴 함수
    cnt = 0
    fxs, fys = [0, 1], [1, 0] # 동, 남
    for fx, fy in zip(fxs, fys):
        nx, ny = x + fx, y + fy
        
        if is_range(nx, ny) and array[x][y] != 0 and array[nx][ny] != 0 and array[x][y] == array[nx][ny]:
            cnt += 1
 
    return cnt 

ans = 0
# 모든 격자 완전 탐색
for x in range (n):
    for y in range (n):
        boom_range = 0
        if grid[x][y] == 0:
            continue
        boom_range = grid[x][y] # 폭발 범위
        test = deepcopy(grid) # 항상 새로운 2차원 배열로 테스트
        
        # 폭발
        for dx, dy in zip(dxs, dys):
            for i in range (boom_range):
                nx, ny = x + dx * i, y + dy * i
                if is_range(nx, ny):
                    test[nx][ny] = 0 # 폭발 처리 = 0
        
        # 중력
        for j in range (n):
            temp = list(filter(lambda x : x > 0, [test[i][j] for i in range (n)]))
            temp = [0] * (n - len(temp)) + temp # 중력 작용
            for i in range (n):
                test[i][j] = temp[i]
        
        # test 배열 한정 모든 격자 완전 탐색
        max_num = 0
        for i in range (n):
            for j in range (n):
                max_num += find_the_optimum(i, j, test)
        
        # 최대값 갱신
        ans = max(ans, max_num)
print(ans)