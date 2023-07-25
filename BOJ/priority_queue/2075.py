# 2075, N번째 큰 수, S2

# N × N의 표에 수 N^2개 채워져 있다. 
# 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다. N = 5일 때의 예를 보자.
# 12	7	9	15	5
# 13	8	11	19	6
# 21	10	26	31	16
# 48	14	28	35	25
# 52	20	32	41	49
# 이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.

# 첫째 줄에 N(1 ≤ N ≤ 1,500)이 주어진다. 다음 N개의 줄에는 각 줄마다 N개의 수가 주어진다. 표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이다.

# 첫째 줄에 N번째 큰 수를 출력한다.

import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []
heapq.heapify(heap)

for _ in range (N):
    row = list(map(int, input().split()))
    for column in row:
        if len(heap) < N:
            heapq.heappush(heap, column)
        else:
            if column > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, column)
print(heap[0])

# 문제를 읽고 나서 굳이 heapq를 써야 하나? 싶어서 걍 배열으로 풀었는데
# 메모리 초과 나서, heapq를 써서 제출했는데 또 메모리 초과...
# 시간초과도 아니고 메모리 초과가 났다는 것은, 메모리가 낭비되고 있다고 판단해서 다시 생각하게 되었다.
# N번째 큰 수만 출력하면 되는 상황에서, row에 있는 값 column이 들어와야 하는지 필요 없는지를 구분했따.
# 현재 heapq에 있는 가장 작은 값보다 (heap[0]) 들어오기로 예정된 column의 값이 더 작다면 저장할 필요가 없으니 버리고
# 큰 값만 넣었다. 그러니까 메모리 초과가 안 났다...