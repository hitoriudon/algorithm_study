import sys

n = int(input())
people = list(map(int, input().split()))
answer = sys.maxsize

for i in range (len(people)):
    dist = 0
    for j in range (len(people)):
        dist += people[j] * abs(i - j)
    if dist < answer:
        answer = dist
        
print(answer)