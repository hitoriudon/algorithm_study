def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def f(x, y, o, e): # row, column, odd, even
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1] # 반시계
    total = 0
    moves = [o, e, o, e] 
    for dx, dy, move in zip(dxs, dys, moves):
        for _ in range (move):
            x, y = x + dx, y + dy
            
            if not is_range(x, y):
                return 0
            
            total += graph[x][y]

    return total

n = int(input())
graph = [list(map(int, input().split())) for _ in range (n)]

max_sum = 0
for i in range (n):
    for j in range (n):
        for k in range (1, n):
            for l in range (1, n):
                max_sum = max(max_sum, f(i, j, k, l))
print(max_sum)