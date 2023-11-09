n = int(input())
before = [list(map(int, input().split())) for _ in range (n)]

r, c = map(int, input().split())
r, c = r - 1, c - 1

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def Print(arr):    
    for line in arr:
        for num in line:
            print(num, end=" ")
        print()
    print()
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0] # 동 서 남 북 (순서 상관 없음)

boom = before[r][c]

for i in range (boom):
    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx * i, c + dy * i
        if is_range(nx, ny):
            before[nx][ny] = 0

after = [[0 for _ in range (n)] for _ in range (n)]

for i in range (n):
    temp = []
    for j in range (n):
        if before[j][i] != 0:
            temp.append(before[j][i])
            
    idx = 0
    for j in range (n - len(temp), n):
        after[j][i] = temp[idx]
        idx += 1

Print(after)