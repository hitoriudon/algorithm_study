n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]

def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < m

tetris = [
    [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], [(0, 1), (1, 0), (1, 1)],
    [(-1, 0), (0, 1), (0, 2)], [(1, 0), (0, -1), (0, -2)], [(1, 0), (0, 1), (0, 2)], [(-1, 0), (0, -1), (0, -2)],
    [(0, 1), (0, 2), (1, 1)], [(0, 1), (0, 2), (-1, 1)], [(1, 0), (2, 0), (1, 1)], [(1, 0), (2, 0), (1, -1)],
    [(1, 0), (1, 1), (2, 1)], [(0, 1), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (1, 2)], [(1, 0), (1, -1), (2, -1)],
    [(1, 0), (2, 0), (2, -1)], [(1, 0), (2, 0), (2, 1)], [(1, 0), (2, 0), (0, 1)], [(0, -1), (1, 0), (2, 0)]
]
ans = 0

for i in range (n):
    for j in range (m): 
        
        for tet in tetris:
            val = grid[i][j]
            
            for x, y in tet:
                nx, ny = i + x, j + y
                if not is_range(nx, ny):
                    break
                val += grid[nx][ny]
                
            ans = max(ans, val)
            
print(ans)

# 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

