# 1021, 회전하는 큐, S4

# 지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.
# 지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 
# 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
loc = list(map(int, input().split()))

queue = deque([i+1 for i in range (n)])

cnt = 0
for x in loc:
    idx = queue.index(x) # 현재 내가 찾아야 하는 값인 x가 queue 어디에 있는지 index()로 확인.
    left, right = idx, len(queue) - idx # left 값이 더 크면 right로 rotate, right 값이 더 크면 left로 rotate.
    if x == queue[0]: #
        queue.popleft()
    elif left <= right:
        queue.rotate(-left) # 왼쪽. - 유념!
        cnt += left
        queue.popleft()
    elif left > right:
        queue.rotate(right) # 오른쪽
        cnt += right
        queue.popleft()
        
print(cnt)

# idx를 생각하는 게 좀 어려웠다.
# 그리고 문제 설명이 진짜 이해가 잘 안 가서, 이해하는 것만 한 시간 걸렸음...
# rotate 쓸 때, 막 쓰지 말고 몇 번 테스트 해보고 써야할 거 같다.