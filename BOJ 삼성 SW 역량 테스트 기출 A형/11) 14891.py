# 14891, 톱니바퀴, G5, 구현
# 시계 방향 1, 반시계 -1
from collections import deque

def f1(flag):
    wheel1, wheel2, wheel3, wheel4 = wheel
    if wheel1[2] == wheel2[6]:
        return flag
    flag[1] = flag[0] * (-1)
    
    if wheel2[2] == wheel3[6]:
        return flag
    flag[2] = flag[1] * (-1)
    
    if wheel3[2] == wheel4[6]:
        return flag
    flag[3] = flag[2] * (-1)
    
    return flag

def f2(flag):
    wheel1, wheel2, wheel3, wheel4 = wheel
    if wheel2[6] != wheel1[2]:
        flag[0] = flag[1] * (-1)
    
    if wheel2[2] == wheel3[6]:
        return flag
    flag[2] = flag[1] * (-1)
    
    if wheel3[2] == wheel4[6]:
        return flag
    flag[3] = flag[2] * (-1)
    
    return flag

def f3(flag):
    wheel1, wheel2, wheel3, wheel4 = wheel
    if wheel3[2] != wheel4[6]:
        flag[3] = flag[2] * (-1)
    
    if wheel3[6] == wheel2[2]:
        return flag
    flag[1] = flag[2] * (-1)
    
    if wheel2[6] == wheel1[2]:
        return flag
    flag[0] = flag[1] * (-1)
    
    return flag

def f4(flag):
    wheel1, wheel2, wheel3, wheel4 = wheel
    if wheel4[6] == wheel3[2]:
        return flag
    flag[2] = flag[3] * (-1)
    
    if wheel3[6] == wheel2[2]:
        return flag
    flag[1] = flag[2] * (-1)
    
    if wheel2[6] == wheel1[2]:
        return flag
    flag[0] = flag[1] * (-1)
    
    return flag

wheel = []
for _ in range (4):
    temp = deque(list(input()) )
    wheel.append(temp)
k = int(input())
move = [list(map(int, input().split())) for _ in range (k)]
f_dict = {1: f1, 2: f2, 3: f3, 4: f4}

for target, dir in move:
    flags = [0 for _ in range (4)]
    
    flags[target - 1] = dir
    flags = f_dict[target](flags)
    
    for i in range (4):
        rot = flags[i]
        wheel[i].rotate(rot)

score = 0
for i in range (4):
    score += int(wheel[i][0]) * 2 ** i
print(score)