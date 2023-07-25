import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range (n)]
cnt, money = 0, 0

while money != k:
    if k < coins[-1]:
        coins.pop()
    else:
        tmp = (k - money) // coins[-1]
        money += coins[-1] * tmp
        cnt += tmp
        coins.pop()
print(cnt)