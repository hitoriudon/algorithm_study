# 15686, 치킨 배달, G5

def find_distance(bbq):
    city_chicken_dist = 0
    for hx, hy in house: # house x, y
        dist = []
        for cx, cy in bbq: # chicken x, y
            chicken_dist = abs(hx - cx) + abs(hy - cy)
            dist.append(chicken_dist)
        city_chicken_dist += min(dist)
    
    return city_chicken_dist

arr = []
def f(level, idx):
    if level == len(bhc):
        if 1 <= len(arr) <= m: 
            candidate = find_distance(arr)
            result.append(candidate)
        return
    arr.append(bhc[idx])
    f(level + 1, idx + 1)
    arr.pop()
    
    f(level + 1, idx + 1)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]
bhc = []
house = []
for i in range (n):
    for j in range (n):
        if grid[i][j] == 2:
            bhc.append((i, j))
        elif grid[i][j] == 1:
            house.append((i, j))
result = []
f(0, 0)

print(min(result))