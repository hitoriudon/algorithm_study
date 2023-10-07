n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
k -= 1
def check(row, start, end):
    for i in range (start, end):
        if grid[row][i] != 0:
            return False
    return True
        
for i in range (n): # row 전체 탐색
    left, right = k, k + m 

    if not check(i, left, right):
        for j in range (left, right):
            grid[i - 1][j] = 1
        break
else:
    for i in range (k, k + m):
        grid[n - 1][i] = 1

for line in grid:
    for num in line:
        print(num, end=" ")
    print()