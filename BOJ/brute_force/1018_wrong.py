# 1018, 체스판 다시 칠하기, S4

# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
# 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board = []
for _ in range (N):
    board.append(list(input()[:-1]))

minimum = 32
for i in range (N - 8 + 1): # 전체 세로
    for j in range (M - 8 + 1): # 전체 가로 # start = board[i][j]
        drawing = 0
        next = ''
        flag = False # for start
        for c in range (8):
            for r in range (8):
                if c == 0 and r == 0: # start point
                    if board[i][j] == 'B': 
                        next = 'W'
                    else: 
                        next = 'B'
                elif board[i+c][j+r] != next: 
                    drawing += 1
                if flag:
                    if next == 'W': 
                        next = 'B'
                    elif next == 'B':
                        next = 'W' 
                flag = True
            if next == 'W':
                next = 'B'
            elif next == 'B':
                next = 'W'
        if minimum > drawing:
            minimum = drawing
print(minimum)

# 예제4를 애초에 못 통과했다. 다른 건 다 맞는데..
# 힌트를 보니 시작이 B일 때랑 W일 때랑 drawing을 구분해야 한다고 한다.

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board = []
for _ in range (N):
    board.append(list(input()[:-1]))
    
minimum = 32
for i in range (N - 8 + 1):
    for j in range (M - 8 + 1):
        drawing = [0, 0] # B, W
        flag = 0
        if board[i][j] == 'W':
            flag = 1
        for c in range (8):
            for r in range (8):
                if (c + r) % 2 == 0:
                    if flag == 0 and board[i+c][j+r] != 'B':
                        drawing[flag] += 1
                    elif flag == 1 and board[i+c][j+r] != 'W':
                        drawing[flag] += 1
                elif (c + r) % 2 == 1:
                    if flag == 0 and board[i+c][j+r] != 'W':
                        drawing[flag] += 1
                    elif flag == 1 and board[i+c][j+r] != 'B':
                        drawing[flag] += 1
        print(drawing)
        if minimum > drawing[flag]:
            minimum = drawing[flag]

print(minimum)        

# 이것도 틀린 코드