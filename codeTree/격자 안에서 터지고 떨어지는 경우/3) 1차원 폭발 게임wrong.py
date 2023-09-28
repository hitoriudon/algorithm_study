import copy
n, m = map(int, input().split())

stack = [int(input()) for _ in range (n)]
if m == 1:
    print(0)
else:
    while True:
        exist = False
        cnt = 1
        temp = copy.deepcopy(stack)
        for i in range (len(temp) - 1):
            if temp[i] == temp[i+1] and (temp[i] == temp[i+1]) != 0:
                temp[i], temp[i+1] = 0, 0
                cnt += 1
        print(temp)
        if cnt >= m:
            exist = True
            temp2 = []
            for num in temp:
                if num != 0:
                    temp2.append(num)
            stack = copy.deepcopy(temp2)
            print(temp2)
        print(stack)
        if not exist:
            break
    print(len(stack))
    for num in stack:
        print(num)

# 포문 스킵 방법

# temp = []
# skip = 0

# for i in range (n):
#     if skip > 0:
#         skip -= 1
#         continue
#     boom = False
#     cnt = 1
#     target = stack[i]
#     for j in range (i + 1, n):
#         if cnt >= m:
#             boom = True
#         next_target = stack[j]
#         if target == next_target:
#             cnt += 1
#         elif target != next_target:
#             break
#     if not boom:
#         temp.append(target)
#     elif boom:
#         skip += 1
