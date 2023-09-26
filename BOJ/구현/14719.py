# 14719, 빗물, G5, 2트

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
grid = [[0 for _ in range (w)] for _ in range (h)] # 2차원 배열
water = 0 # ans

# 1) input을 토대로 2차원 배열로 만듦
for j in range (w): 
    for i in range (blocks[j]):
        grid[h - (i + 1)][j] = 1 # 블록이 있으면 값이 1

# 2) 이중 for문으로 좌표 완전 탐색 진행
for i in range (h):
    for j in range (w):
        if grid[i][j] != 1: # 좌표값이 1이 아닐 때에만 진행 (어차피 블록에는 빗물이 안 쌓이니까)
            left, right = False, False # Flag
            # left check
            for k in range (j):
                if grid[i][k] == 1:
                    left = True
                    break
            for k in range (j, w):
                if grid[i][k] == 1:
                    right = True
                    break
            if left and right:
                water += 1
                
print(water)