string = input()

do_not_reverse = False
ans = []
reverse_array = []
for s in string:
    if s == '<' or s == ' ': # '<'가 나오면, 안 뒤집기
        for _ in range (len(reverse_array)):
            ans.append(reverse_array.pop())
        ans.append(s)
        if s == '<':    
            do_not_reverse = True
    elif s == '>':
        do_not_reverse = False
        ans.append(s) 
    elif do_not_reverse:
        ans.append(s)
    elif not do_not_reverse:
        reverse_array.append(s)

for _ in range (len(reverse_array)):
    ans.append(reverse_array.pop())
print(''.join(ans))