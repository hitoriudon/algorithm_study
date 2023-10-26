action = input()
ans = 0
stack = []

o, c = '(', ')'
for i in range (len(action)):
    # '(' -> append
    if action[i] == o:
        stack.append(o)
    
    # ')' and action[i-1] + action[i] == '()' -> lazer
    elif action[i-1] + action[i] == '()':
        stack.pop()
        ans += len(stack)
        
    # ')' and action[i-1] + action[i] != '()' -> stick end
    elif action[i-1] + action[i] != '()':
        stack.pop()
        ans += 1
print(ans)