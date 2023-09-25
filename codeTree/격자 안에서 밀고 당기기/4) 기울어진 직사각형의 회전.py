from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split()) # 1 <= r & c <= n 조건에 의해 각각 -1씩 해줘야 함. 
r, c = r - 1, c - 1

dxs, dys, current_dir = [-1, -1, 1, 1], [1, -1, -1, 1], 0
ms = [m1, m2, m3, m4]

rail = deque()  
for m in ms:
    nr, nc = 0, 0
    for i in range (1, m + 1):
        nr, nc = r + dxs[current_dir] * i, c + dys[current_dir] * i # 좌표
        rail.append((nr, nc))
    current_dir += 1
    r, c = nr, nc

rail.rotate(1)
rail2 = deque(rail)

if dir == 1:
    rail2.rotate(-1)
elif dir == 0:
    rail2.rotate(1)

values = [] 
for x, y in rail2:
    values.append(grid[x][y])

idx = 0
for value in values:
    x, y = rail[idx]
    grid[x][y] = value
    idx += 1
    
def Print():
    for l in grid:
        for i in l:
            print(i, end=" ")
        print()
        
Print()