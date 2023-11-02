from collections import deque

testcase = int(input())

for _ in range (testcase):
    n = int(input())
    cards = deque(map(str, input().split()))
    ans = deque()
    
    first = cards.popleft()
    ans.append(first)
    
    for card in cards:
        if card <= first:
            first = card
            ans.appendleft(card)
        elif card > first:
            ans.append(card)
    
    print(''.join(ans))