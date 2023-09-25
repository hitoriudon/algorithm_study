import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split()))) # 정렬이 안 되면 투포인터 의미가 없음
x = int(input())
answer = 0

start, end = 0, len(nums) - 1

while start < end:
    temp = nums[start] + nums[end]
    if temp == x:
        answer += 1
        start += 1
        end -= 1
    elif temp > x: # 값을 줄여주기 위해 end -= 1 
        end -= 1
    elif temp < x:
        start += 1
        
print(answer)