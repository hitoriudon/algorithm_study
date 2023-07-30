# 2775, 부녀회장이 될테야, B1
testcase = int(input())

for _ in range (testcase):
    floor = int(input())
    number = int(input())
    base = []
    base.append([i + 1 for i in range (number)])
    answer = 0
    
    for i in range (1, floor + 1):
        i_floor = []
        for j in range (number):
            i_floor.append(sum(base[i-1][:j+1]))
        base.append(i_floor)
    print(base[floor][number - 1])