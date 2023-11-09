string = input()

ans = 0

for i in range (len(string)):
    ans += 1
    
    char = string[i]
    if char == '-':
        ans -= 1
    
    elif char == '=':
        ans -= 1
        if string[i - 2] + string[i - 1] == 'dz':
            ans -= 1
    
    elif char == 'j':
        if string[i - 1] == 'l' or string[i - 1] == 'n':
            ans -= 1

print(ans)