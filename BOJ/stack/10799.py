sticks = input()

ans = 0
stack = []
is_lazer = False
o, c = '(', ')' # open, close

for s in sticks:
    # (가 들어오면 stack에 추가
    if s == o:
        stack.append(o)
        is_lazer = True
    # )가 들어오면 스택 팝 해주고 ans += 1, 단 앞에가 (가 아니여야 함
    elif s == c and not is_lazer:
        stack.pop()
        ans += 1
        is_lazer = False
    # )가 들어오면 스택 팝 해주고 ans += len(stack). 단 앞에가 (여야 함.
    elif s == c and is_lazer:
        stack.pop()
        ans += len(stack)
        is_lazer = False    

print(ans)