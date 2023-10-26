from collections import deque

n, k = map(int, input().split())
people = deque([i + 1 for i in range (n)])
ans = '<'
for i in range (n):
    
    # 뒤로 보내기
    for _ in range (k - 1): 
        people.append(people.popleft())
    
    target = people.popleft()
    
    ans += str(target)
    
    if i < n - 1:
        ans += ', '

print(ans + '>')