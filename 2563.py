# 색종이 실버 5 구현
import sys
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range (100)] for _ in range (100)]

for _ in range (n):
    x, y = map(int, input().split())
    for i in range (x-1, x+9):
        for j in range (y-1, y+9):
            board[i][j] = 1
total = 0
for line in board:
    total += sum(line)
print(total)