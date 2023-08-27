n, m = map(int, input().split())
words = [list(input()) for _ in range (n)]

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
lee = ['L', 'E', 'E']
answer = 0

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for x in range (n):
    for y in range (m):
        
        for dx, dy in zip(dxs, dys):
            dots = [(x + dx * i, y + dy * i) for i in range (3)]
            
            cnt = 0
            for i in range (3):
                nx, ny = dots[i]
                if is_range(nx, ny) and words[nx][ny] == lee[i]:
                    cnt += 1
            
            if cnt == 3:
                answer += 1
print(answer)