n, count = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]

boom_column = [int(input()) - 1 for _ in range (count)]

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북

for bomb in boom_column:
    x, y = 0, bomb # start index
    find = False
    for i in range (n):
        if grid[i][y] != 0:
            x = i
            find = True
            break
        
    if find: # 그리드의 값이 0이면 아무 일도 안 일어나야 함
        for i in range (grid[x][y]): # 범위
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx * i, y + dy * i
                
                if is_range(nx, ny):
                    grid[nx][ny] = 0
        
        # 중력
        for j in range (n):
            temp = list(filter(lambda x : x > 0, [grid[i][j] for i in range (n)]))
            temp = [0] * (n - len(temp)) + temp
            for i in range (n):
                grid[i][j] = temp[i]

for l in grid:
    for n in l:
        print(n, end=" ")
    print()
print()