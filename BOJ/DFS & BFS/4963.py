n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
k = int(input())
quest = [list(map(int, input().split())) for _ in range (k)]

for i, j, x, y in quest:
    result = 0
    for m in range (i - 1, x):
        for n in range (j - 1, y):
            result += grid[m][n]
    print(result)