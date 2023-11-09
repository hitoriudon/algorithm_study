r, c = map(int, input().split())    
b = [list(map(str, input().split())) for _ in range (r)]
answer = 0

start_color = b[0][0]
end_color = ''
if start_color == 'W': 
    end_color = 'B'
elif start_color == 'B':
    end_color = 'W'

for i in range (1, r):
    for j in range (1, c):
        if b[i][j] != start_color:
            for k in range (i+1, r):
                for l in range (j+1, c):
                    if b[k][l] == start_color and k + 1 < r and l + 1 < c and b[r-1][c-1] == end_color:  
                        answer += 1
            
print(answer)