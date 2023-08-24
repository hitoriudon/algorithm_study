r, c = map(int, input().split())    
b = [list(map(str, input().split())) for _ in range (r)]
answer = 0

current = b[0][0]
target = ''
if current == 'W': 
    target = 'B'
elif current == 'B':
    target = 'W'

for i in range (1, r):
    for j in range (1, c):
        if b[i][j] != current:
            for k in range (i+1, r):
                for l in range (j+1, c):
                    if b[k][l] == current and k + 1 < r and l + 1 < c and b[r-1][c-1] == target:  
                        answer += 1
            
print(answer)