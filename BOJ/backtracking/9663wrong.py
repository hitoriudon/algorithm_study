# 9663, N-Queen, G4, 브루트 포스?

def is_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

n = int(input())

grid = []
i = 1
for _ in range (n):
    tmp = []
    for _ in range (n):
        tmp.append(i)
        i += 1
    grid.append(tmp)
for line in grid:
    print(line)
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

ans = []
for x in range (n):
    for y in range (n):
        test_grid = [[0 for _ in range (n)] for _ in range (n)]
        test_grid[x][y] = 1
        
        for k in range (1, n):
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx * k, y + dy * k
                if is_range(nx, ny) and test_grid[nx][ny] == 0:
                    test_grid[nx][ny] = 1
        for i in range (n):
            for j in range (n):
                if test_grid[i][j] == 0:
                    basis, target = grid[x][y], grid[i][j]
                    if basis > target:
                        ans.append((target, basis))
                    else:
                        ans.append((basis, target))
        
# print(sorted(list(set(ans))))
print(len(set(ans)))

            