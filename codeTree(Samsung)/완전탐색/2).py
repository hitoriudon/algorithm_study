string = input()    
answer = 0

for i in range (len(string)):
    if string[i] == '(':
        for j in range (i, len(string)):
            if string[j] == ')':
                answer += 1
print(answer)