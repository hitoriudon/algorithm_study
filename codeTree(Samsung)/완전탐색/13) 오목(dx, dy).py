import sys

board = [list(map(int, input().split())) for _ in range (19)]

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def is_range(x, y):
    return x >= 0 and x < 19 and y >= 0 and y < 19

find_flag = False
for x in range (19): # 세로
    for y in range (19): # 가로
        
        for dx, dy in zip(dxs, dys):
            dots = [(x + dx * i, y + dy * i) for i in range (5)]
            points = []
            
            for i in range(5):
                nx, ny = dots[i]
                if is_range(nx, ny) and board[nx][ny] != 0:
                    points.append(board[nx][ny])
                    
            if len(points) == 5 and len(set(points)) == 1:
                ax, ay = dots[2]
                print(board[ax][ay])
                print(ax + 1, ay + 1)
                find_flag = True
                sys.exit()
print(0)