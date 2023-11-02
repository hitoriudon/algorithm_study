# 에르난 질문. import sys 없으면 시간 초과
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
skill = list(map(int, input().split()))
cards = deque([i for i in range (n)])

ans = deque()

i = n
for num in skill:
    i -= 1
    if num == 1:
        ans.appendleft([i, cards.popleft()])
    elif num == 2:
        cards.rotate(-1)
        ans.appendleft([i, cards.popleft()])
        cards.rotate(1)
    elif num == 3:
        ans.appendleft([i, cards.pop()])
    
ans = sorted(list(ans), key = lambda x: x[1])

for i in range (n):
    num = ans[i][0] + 1
    print(num, end=" ")
print()