n = int(input())
command = list(map(str, input().split()))
x, y = 1, 1 # {x: [U, D]}, {y: [L, R]}  

# my
for c in command:
    if 1 <= y < n and c == 'R':
        y += 1
    elif 1 < y <= n and c == 'L':
        y -= 1
    elif 1 <= x < n and c == 'D':
        x += 1
    elif 1 < x <= n and c == 'U':
        x -= 1
print(x, y)

# another
dx = [0, 0, -1, 1] # L, R, U, D
dy = [-1, 1, 0, 0] # L, R, U, D
direction = ['L', 'R', 'U', 'D']

for c in command:
    for i in range (len(direction)):
        if c == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    else:
        x, y = nx, ny
print(x, y)