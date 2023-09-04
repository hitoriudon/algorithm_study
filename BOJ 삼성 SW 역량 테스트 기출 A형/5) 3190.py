# 3190, 뱀, G4
import sys
from collections import deque
input = sys.stdin.readline

def is_range(x, y): # 벽에 부딪힌 경우 (index out)
    return x >= 0 and x < size and y >= 0 and y < size

def touch(x, y): # 뱀 머리가 뱀에 맞은 경우 (deque 안에 뱀 좌표가 있으면)
    for sx, sy in list(snake):
        if x == sx and y == sy:
            return True # 종료시켜라
    return False # 터치 안 됐다

size = int(input())
apples = []
for _ in range (int(input())):
    r, c = map(int, input().split())
    apples.append((r - 1, c - 1)) # 맨 왼쪽 맨 위가 (1, 1)라는 문제 조건
    
moves = {} # 그냥 딕셔너리 썼음 keys() 메소드 쓰기 편하니까
for _ in range (int(input())):
    t, dir = map(str, input().split())
    moves[int(t)] = dir

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북

board = []
for _ in range (size):
    board.append([0] * size)

for ax, ay in apples: # 비었으면 0, 사과 있는 곳은 1
    board[ax][ay] = 1

dir = 0 # 초기 방향은 오른쪽
x, y, time = 0, 0, 0 # 뱀 머리 x좌표, 뱀 머리 y좌표, 시간
snake = deque([(0, 0)]) # 최초 뱀 머리 위치

while True:
    time += 1
    x, y = x + dxs[dir], y + dys[dir]
    
    if is_range(x, y) and touch(x, y) == False:
        snake.append((x, y))
        if board[x][y] == 0:
            snake.popleft()
        elif board[x][y] == 1:
            board[x][y] = 0
            
        if time in moves.keys():
            if moves[time] == 'L':
                dir = (dir - 1) % 4
            elif moves[time] == 'D':
                dir = (dir + 1) % 4
    else:        
        print(time)    
        break

# 내가 자체적으로 만든 테스트케이스는 예상 값대로 잘 나왔는데
# 자꾸 틀렸습니다하길래 뭐가 문제인지 생각해보다가
# 사과 먹었으면 사과를 없애야 하는데 그걸 빼먹었음
# 바로 추가하니까 됐다
# 1시간 조금 안 걸린듯