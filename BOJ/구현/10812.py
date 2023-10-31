from collections import deque
n, m = map(int, input().split())
nums = [str(i+1) for i in range (n)] # for join
for _ in range (m):
    begin, end, mid = map(int, input().split())
    copy = deque(nums[begin - 1: end])
    copy.rotate(-(mid-begin))
    copy = list(copy)
    for i in range (end - begin + 1):
        nums[begin - 1 + i] = copy[i]
    print(nums)
print(*nums)
# print(' '.join(nums))