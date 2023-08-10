# 369, B3
import sys
input = sys.stdin.readline

n = int(input())
clap = 0
nums = [str(i) for i in range (1, n + 1)]

for num in nums:
    for index in range (len(num)):
        if num[index] == '3' or num[index] == '6' or num[index] == '9': 
            clap += 1

print(clap)