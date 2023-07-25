import sys
input = sys.stdin.readline

row, column = map(int, input().split())
table = []
for _ in range (row):
    table.append(input())
    
max_length = max(row, column)
maxi = 0

for i in range (row):
    for j in range (column):
        for k in range (max_length):
            if i+k < row and j+k < column:    
                if table[i][j] == table[i+k][j] == table[i][j+k] == table[i+k][j+k]:
                    maxi = max(maxi, (k+1)**2)
print(maxi)
