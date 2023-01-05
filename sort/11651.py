import sys

N = int(input())
dots = []
for _ in range (N):
    x, y = list(map(int, sys.stdin.readline().split()))
    dots.append([x,y])

for dot in dots: # x, y = y, x
    dot[0], dot[1] = dot[1], dot[0] # sort()는 [0]을 기준으로 정렬하기 때문에

dots.sort()

for dot in dots: # x, y = y, x
    dot[0], dot[1] = dot[1], dot[0] # 다시 원래대로
    
for dot in dots:
    print(dot[0], dot[1])