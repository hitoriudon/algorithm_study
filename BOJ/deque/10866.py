# 10866, 덱, S4

# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여덟 가지이다.
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력해야 하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque([])
for _ in range (N):
    cmd = input().split()
    if cmd[0] == 'pop_front': 
        print(queue.pop() if len(queue) != 0 else -1)
    elif cmd[0] == 'pop_back': 
        print(queue.popleft() if len(queue) != 0 else -1)
    elif cmd[0][0] == 's': # size
        print(len(queue))
    elif cmd[0][0] == 'e': # empty
        print(1 if len(queue) == 0 else 0)
    elif cmd[0][0] == 'f': # front
        print(queue[-1] if len(queue) != 0 else -1)
    elif cmd[0][0] == 'b': # back
        print(queue[0] if len(queue) != 0 else -1)
    else:
        if cmd[0][5] == 'f': queue.append(cmd[1]) # push_front
        else: queue.appendleft(cmd[1]) # push_back
        
# 비슷한 유형이 많았어서.. 그냥 쉽게 이젠 풀리는 유형.
