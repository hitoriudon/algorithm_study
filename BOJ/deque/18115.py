# 18115, 카드 놓기, S3
from collections import deque

n = int(input())
skill = list(map(int, input().split()))

card = deque([i for i in range (n)])
answer = deque()

for num in skill:
    if num == 1:
        answer.appendleft(card.popleft())
    elif num == 2:
        card.rotate(-1)
        answer.appendleft(card.popleft())
        card.rotate(1)
    elif num == 3:
        answer.appendleft(card.pop())

result = [0 for _ in range (n)]
value = 1
for idx in answer:
    result[idx] = value
    value += 1

for num in result:
    print(num, end=" ")
print()