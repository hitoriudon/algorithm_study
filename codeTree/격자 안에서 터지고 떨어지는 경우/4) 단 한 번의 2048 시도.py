grid = [list(map(int, input().split())) for _ in range (4)]
dir = input()   

def Print():
    for line in grid:
        for num in line:
            print(num, end=" ")
        print()
    print()

def left():
    for line in grid:
        temp = list(filter(lambda x: x > 0, line))
        skip_idx = -1
        temp2 = []
        for i in range (len(temp) - 1):
            if i == skip_idx:
                continue
            if temp[i] == temp[i + 1]:
                temp2.append(temp[i] + temp[i + 1])
                skip_idx = i + 1
            elif temp[i] != temp[i + 1] and temp[i] != 0:
                temp2.append(temp[i])
                
        if skip_idx != len(temp) - 1:
            temp2.append(temp[len(temp) - 1])
        
        for _ in range (len(temp2), 4):
            temp2.append(0)
        
        for i in range (4):
            line[i] = temp2[i]

def right():
    for line in grid:
        temp = list(filter(lambda x: x > 0, line))
        skip_idx = -1
        temp2 = []
        
        for i in range (len(temp) - 1, 0, -1):
            if i == skip_idx:
                continue
            if temp[i] == temp[i - 1]:
                temp2.append(temp[i] + temp[i - 1])
                skip_idx = i - 1
            elif temp[i] != temp[i - 1] and temp[i] != 0:
                temp2.append(temp[i])
        if (skip_idx != 0 or len(temp) == 1) and len(temp) != 0:
            temp2.append(temp[0])
        
        for _ in range (len(temp2), 4):
            temp2.append(0)
         
        for i in range (4):
            line[-(i+1)] = temp2[i]

def up():
    for j in range (4):
        temp = list(filter(lambda x: x > 0, [grid[i][j] for i in range (4)]))
        skip_idx = -1
        temp2 = []
        for i in range (len(temp) - 1):
            if i == skip_idx:
                continue
            if temp[i] == temp[i + 1]:
                temp2.append(temp[i] + temp[i + 1])
                skip_idx = i + 1
            elif temp[i] != temp[i + 1] and temp[i] != 0:
                temp2.append(temp[i])
        
        if skip_idx != len(temp) - 1:
            temp2.append(temp[len(temp) - 1])
        
        for _ in range (len(temp2), 4):
            temp2.append(0)
        
        for i in range (4):
            grid[i][j] = temp2[i]

def down():
    for j in range (4):
        temp = list(filter(lambda x: x > 0, [grid[i][j] for i in range (4)]))
        skip_idx = -1
        temp2 = []
        for i in range (len(temp) - 1, 0, -1):
            if i == skip_idx:
                continue
            if temp[i] == temp[i - 1]:
                temp2.append(temp[i] + temp[i - 1])
                skip_idx = i - 1
            elif temp[i] != temp[i - 1] and temp[i] != 0:
                temp2.append(temp[i])
        
        if (skip_idx != 0 or len(temp) == 1) and len(temp) != 0:
            temp2.append(temp[0])
        
        for _ in range (len(temp2), 4):
            temp2.append(0)
        
        for i in range (4):
            grid[-(i+1)][j] = temp2[i]

dic = {'L': left, 'R': right, 'U': up, 'D': down}
dic[dir]()
Print()