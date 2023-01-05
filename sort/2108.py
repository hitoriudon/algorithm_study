# 2108, 통계학, S3

# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys
N = int(sys.stdin.readline())
indexes = [0]*8001
total, nums, mosts, rng = 0, [], [], 0
for i in range (N):
    num = int(sys.stdin.readline())
    indexes[num+4000] += 1
    nums.append(num)
    total += num
    
most = max(indexes)

for i in range (8001):
    if indexes[i] != 0:
        if indexes[i] == most:
            mosts.append(i-4000)
            nums.sort()
        
print(round(total/N))
print(nums[N//2])
print(mosts[1] if len(mosts)>=2 else mosts[0])
print(nums[N-1] - nums[0])


'''
N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range (N)]
numbers.sort()
print(round(sum(numbers)/N))
print(numbers[N//2])

max_num, arr = 0, []
for n in numbers:
    temp = numbers.count(n)
    if temp != 1 and temp > max_num:
       max_num = temp
for n in numbers:
    if numbers.count(n) == max_num:
        arr.append(n)
arr = sorted(list(set(arr)))
if max_num==0:
    print(numbers[1])
else: 
    print(arr[1] if len(arr)>=2 else arr[0])
print(numbers[N-1] - numbers[0])


'''