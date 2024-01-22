n = int(input())
nums = list(map(int, input().split()))

count = [0 for _ in range (101)]

for num in nums:
    count[num] += 1

progress = 0
second_min_value = -1
for num in set(sorted(nums)):
    progress += 1
    if progress == 2:
        second_min_value = num
        break

if count[second_min_value] > 1 or second_min_value == -1:
    print(-1)
else:
    for i in range (n):
        if nums[i] == second_min_value:
            print(i + 1)
            