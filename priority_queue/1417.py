# 1417, 국회의원 선거, S5

# 다솜이는 사람의 마음을 읽을 수 있는 기계를 가지고 있다. 다솜이는 이 기계를 이용해서 2008년 4월 9일 국회의원 선거를 조작하려고 한다.
# 다솜이의 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다. 어떤 사람이 누구를 찍을 지 정했으면, 반드시 선거때 그 사람을 찍는다.
# 현재 형택구에 나온 국회의원 후보는 N명이다. 다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.
# 다솜이는 기호 1번이다. 다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다. 
# 다른 모든 사람의 득표수 보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선된다.
# 예를 들어서, 마음을 읽은 결과 기호 1번이 5표, 기호 2번이 7표, 기호 3번이 7표 라고 한다면, 
# 다솜이는 2번 후보를 찍으려고 하던 사람 1명과, 3번 후보를 찍으려고 하던 사람 1명을 돈으로 매수하면, 국회의원에 당선이 된다.
# 돈으로 매수한 사람은 반드시 다솜이를 찍는다고 가정한다.
# 다솜이가 매수해야 하는 사람의 최솟값을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 후보의 수 N이 주어진다. 
# 둘째 줄부터 차례대로 기호 1번을 찍으려고 하는 사람의 수, 기호 2번을 찍으려고 하는 수, 이렇게 총 N개의 줄에 걸쳐 입력이 들어온다. 
# N은 50보다 작거나 같은 자연수이고, 득표수는 100보다 작거나 같은 자연수이다.

# 첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값을 출력한다.

import sys, heapq
input = sys.stdin.readline

N = int(input())

heap = []
candidate = [int(input()) for _ in range (N)]

for i in range (1, N): # maxheap 만들기
    heapq.heappush(heap, (-candidate[i], candidate[i], i)) # 튜플 첫번째 요소로 최소 힙 정렬하니까, -를 붙여줌. 튜플 마지막 요소는 인덱스 값.
# 다솜이 인덱스는 힙(list)의 가장 마지막에 붙여야 함... 그냥 그게 맞음 디버깅해보니까 그럼
heap.append((-candidate[0], candidate[0], 0))

for i in range (N): # 다솜이 노드가 현재 heap에서 어디 인덱스에 위치하는지 파악
    if heap[i][2] == 0:
        dasom_idx = i
        break

cnt = 0
maximum = max(candidate)
#print("First: ", heap)
#print("dasom: ", dasom_idx)
if N == 1:
    print(0)
elif candidate.count(maximum) > 1 and candidate[0] == maximum:
    print(1)
else:
    while dasom_idx > 0:
        if dasom_idx % 2 == 0:
            upper_idx= (dasom_idx - 1) // 2
        else:
            upper_idx = dasom_idx // 2
        
        diff = ((heap[upper_idx][1] - heap[dasom_idx][1]) // 2) + 1 
        
        # tuple 값을 직접 더하고 뺄 수 없어서, heap에 들어있는 tuple의 값을 직접 변경
        heap[upper_idx] = ((heap[upper_idx][1] - diff)* (-1), heap[upper_idx][1] - diff, heap[upper_idx][2])
        heap[dasom_idx] = ((heap[dasom_idx][1] + diff)* (-1), heap[dasom_idx][1] + diff, heap[dasom_idx][2])
        # heapq.heapify(heap) # 이렇게 하면 안 됨 그냥 자리만 서로 바꿔야 함
        heap[upper_idx], heap[dasom_idx] = heap[dasom_idx], heap[upper_idx]
        #print(heap)
        #print("diff: ", diff)
        #print()
        cnt += diff # 표 카운트
        dasom_idx = upper_idx
    
    print("answer: ", cnt)

# 진짜 내 코드 반례의 경우의 수가 너무 많았던 문제. 그냥 내가 멍청하게 푼 것 같은 느낌이 든다.
# 반례 1,6,6,6,6일 때를 찾아서 heapify를 매번 하면 안 된다는 걸 알았다. 그냥 서로 위치만 바꿔줘야 함.