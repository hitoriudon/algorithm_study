# 13458, 시험 감독, B2

n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

total = 0
for student in students:
    student -= b
    total += 1
    
    if student <= 0:
        continue
    temp, x = student / c, student // c
    if x < temp < x + 1: # 소수점 있다는 뜻. import math의 ceil()을 못 쓴다고 가정하면.
        total += x + 1
    else:
        total += x
    
print(total)