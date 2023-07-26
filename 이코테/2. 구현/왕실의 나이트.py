loc = input()
x, y = int(loc[1]), ord(loc[0]) - 96
direction = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
cnt = 0
for d in direction:
    nx = x + d[0]
    ny = y + d[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        cnt += 1
print(cnt)