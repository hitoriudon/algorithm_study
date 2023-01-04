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