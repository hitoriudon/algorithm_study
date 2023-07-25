# 15235, 피자 올림피아드, S5

# 보통 올림피아드 결선에서는 참가자에게 피자를 나눠줍니다. 음식이 도착하면, 참가자는 피자를 얻기 위해 줄을 섭니다.
# 각 학생은 자신의 순서가 돌아오면 한 조각의 피자를 받습니다. 
# 문제는 몇몇 사람의 경우 배가 부르려면 한 조각보다 많이 피자를 먹어야 하고, 
# 따라서 첫 번째 조각을 받은 후 피자를 더 받기 위해 또 줄을 선다는 것입니다.
# 각 참가자가 배가 부르려면 먹어야 하는 조각의 수가 주어질 때, 모든 사람을 배부르게 하려면 얼마나 걸리는지 계산합시다. 
# 매 초마다 피자 조각을 나눠주며 이미 배가 부른 참가자는 다시 줄을 서지 않습니다.

# 첫 줄에 참가자의 수를 나타내는 하나의 정수 N이 주어집니다. (N <= 1000)
# 두 번째 줄에 N개의 정수가 공백으로 구분되어 주어집니다. 각 참가자를 배부르게 하기 위해 필요한 피자 조각의 수입니다. 
# 각 참가자는 최소 1 조각에서 최대 100 조각의 피자를 필요로 합니다.

# N개의 정수를 공백으로 구분해 한 줄에 출력합니다. 이는 그 참가자가 필요로 하는 모든 조각을 받은 시간입니다.

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

pizza_list = list(map(int, input().split()))
students = deque([[i, pizza_list[i]] for i in range (N)]) # list(몇번째 학생 인덱스 값, 학생의 원하는 피자 수)
answer = ['0'] * N # join() 쓰려고 str
time = 0
while len(students) != 0:
    time += 1
    if students[0][1] != 1:
        students[0][1] -= 1
        students.rotate(-1)
    else: # 1일 때 pop
        answer[students[0][0]] = str(time)
        students.popleft()
print(' '.join(answer))