import sys

N = int(input())
dots = []
for _ in range (N):
    x, y = list(map(int, sys.stdin.readline().split()))
    dots.append([x,y])

dots.sort()
    
for dot in dots:
    print(dot[0], dot[1])