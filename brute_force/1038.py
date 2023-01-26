# 1038, 감소하는 수, G5

# 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 
# 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. 
# N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

# 첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

# 첫째 줄에 N번째 감소하는 수를 출력한다.

import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())

nums = []
for i in range (10):
    for combi in combinations(range(0, 10), i+1):
        nums.append(int("".join(map(str, sorted(list(combi), reverse=True)))))
print(-1 if N >= len(nums) else sorted(nums)[N])

# 시간 초과
'''
import sys
input = sys.stdin.readline
N = int(input())

if 0 <= N <= 10: 
    print(N)

else:
    cnt = 10
    key = True
    i = 11
    while i <= 9876543210:
        nums = list(map(int, list(str(i))))
        if len(set(nums)) == len(nums) and sorted(nums, reverse=True) == nums:     # 중복이 있으면 감소하는 수가 아님
            cnt += 1
        if cnt == N:
            print(i)
            key = False
            break
        i += 1
    if key:
        print(-1)
'''

# 조합 진짜 생각도 못 하고 있었네... 진짜...