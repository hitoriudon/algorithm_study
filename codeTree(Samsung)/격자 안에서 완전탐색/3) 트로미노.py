n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range (n)]

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

max_num = 0

dot1 = [(1,0), (1,0), (-1,0), (-1,0), (0,1), (1,0)]
dot2 = [(0,1), (0,-1), (0,-1), (0,1), (0,2), (2,0)]

for i in range (n):
    for j in range (m):
        for k in range (6):
            nx1, ny1 = dot1[k]
            nx2, ny2 = dot2[k]
            
            if is_range(i + nx1, j + ny1) and is_range(i + nx2, j + ny2):
                p1, p2, p3 = nums[i][j], nums[i + nx1][j + ny1], nums[i + nx2][j + ny2]
                max_num = max(max_num, p1 + p2 + p3)
print(max_num)                