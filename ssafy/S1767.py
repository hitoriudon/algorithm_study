dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
def isRange(x, y):
    return 0 <= x < n and 0 <= y < n

def check(x, y):
    global n 
    direction = [0, 0, 0, 0]
    d = 0
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        length = 0
        
        while isRange(nx, ny):
            if grid[nx][ny]:
                break
            
            nx += dx
            ny += dy
            length += 1
    
        if not (isRange(nx, ny)):
            direction[d] = length
        
        d += 1
        
    return direction

def connect(x, y, d, toggle):
    global n
    nx, ny = x + dxs[d], y + dys[d]
    
    while isRange(nx, ny):
        grid[nx][ny] = toggle
        nx += dxs[d]
        ny += dys[d]
        
def recursive(cur, minSum, resultCount):
    global result
    
    if resultCount > result[0]:  
        result[0] = resultCount
        result[1] = minSum
    elif resultCount == result[0]:  
        if result[1] > minSum:
            result[1] = minSum
    
    if cur == coreCount:
        return
    
    x, y = core[cur][0], core[cur][1]
    
    direction = check(x, y)
    
    for d in range (4):
        if direction[d] == 0:
            continue
        
        connect(x, y, d, 1) # 연결
        recursive(cur + 1, minSum + direction[d], resultCount + 1)
        connect(x, y, d, 0) # 연결 해제
        
    recursive(cur + 1, minSum, resultCount)


T = int(input())
for t in range (1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range (n)]
    
    core = []
    coreCount = 0
    
    for i in range (1, n - 1):
        for j in range (1, n - 1):
            if grid[i][j] == 1:
                core.append((i, j))
                coreCount += 1
    
    result = [0, 0]
    recursive(0, 0, 0)
    
    print(f'#{t} {result[1]}')