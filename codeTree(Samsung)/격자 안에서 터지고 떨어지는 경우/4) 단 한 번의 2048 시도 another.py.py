def Print():
    for l in grid:
        for n in l:
            print(n, end=" ")
        print()
    print()

grid = [list(map(int, input().split())) for _ in range (4)]
dir = input()
dic = {'L': 0, 'D': 1, 'R': 2, 'U': 3} # 시계 방향으로 회전

for _ in range (dic[dir]):
    grid = list(zip(*grid[::-1])) # 회전
    
for i in range (4):
    grid[i] = list(grid[i]) # tuple -> list

for line in grid:
    temp = list(filter(lambda x : x > 0, line))
    skip_idx = -1
    temp2 = []
    
    for i in range (len(temp) - 1):
        if i == skip_idx:
            continue
        if temp[i] == temp[i + 1]:
            temp2.append(temp[i] + temp[i + 1])
            skip_idx = i + 1
        elif temp[i] != temp[i + 1]:
            temp2.append(temp[i])
        
    if skip_idx != len(temp) - 1:
        temp2.append(temp[len(temp) - 1])
    
    for _ in range (len(temp2), 4):
        temp2.append(0)
    
    for i in range (4):
        line[i] = temp2[i]

for _ in range (4 - dic[dir]):
    grid = list(zip(*grid[::-1])) # 원상복귀

Print()