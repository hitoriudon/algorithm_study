# 11279, 최대 힙, S2

# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
# 입력되는 자연수는 2^31보다 작다.

# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
heap = PriorityQueue()

nums = [int(input()) for _ in range (N)] # 미리 다 input 받음
natural_numbers = sorted(list(set(nums))[1:], reverse=True) # 0 빼고 자연수들만 정리

dict1 = { natural_numbers[i] : i for i in range (len(natural_numbers))} # 키 값인 natural_numbers의 값이 클 수록, value 값인 우선순위의 값이 작다.

for n in nums:
    if n == 0:
        print(0 if heap.empty() else (heap.get())[1])
    else:
        heap.put((dict1[n], n))
        
        
# 최소 힙은 쉬웠는데 최대 힙은 진짜 어렵네... 우선 미리 다 인풋을 받은 이유는, 자연수들의 우선 순위를 정하기 위해서다. 
# 큰 자연수 순서대로 순위를 매겼고(딕셔너리), 이제 본격적으로 출력을 시작했다.
# 자연수가 들어오면(else일 때) 그 자연수가 딕셔너리에서 몇번째 우선 순위인지를 알 수 있는 값 dict1[n]를 tuple의 첫번째 인덱스에 넣었고,
# 그 자연수의 값 n은 tuple의 두번째 인덱스에 넣었다.
# PriorityQueue