n = int(input())
nums = list(map(int, input().split()))

max_num = 0
for i in range (n):
    for j in range (i+2, n):
        max_num = max(max_num, nums[i] + nums[j])
print(max_num)